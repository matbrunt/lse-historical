# coding: utf-8
import requests
import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from time import sleep

from helpers import utils


logger = utils.get_logger(__name__)
SCRAPE_WAIT_SECS = 3


def fetch_page(url, s):
    logger.info('Fetching %s' % url)
    r = s.get(url)
    return BeautifulSoup(r.text, "html.parser")


def parse_first_page(url, s):
    soup = fetch_page(url, s)
    content = parse_table(soup)
    last_page = get_last_page(soup)
    
    return content, last_page


def get_last_page(soup):
    paging = soup.select_one('div.paging > p:nth-of-type(1)').string
    m = re.search(r'of (\d+)$', paging)
    if m:
        return int(m.groups()[0])
    return None


def parse_company(el):
    symbolId = re.search(r'\/(\w+)\.html', el.get('href'))
    if symbolId:
        symbolId = symbolId.group(1)
    
    return (el.string, symbolId)


def parse_table(soup):
    data = []
    rows = soup.find("table", class_="table_dati").find("tbody").findAll("tr")
    for tr in rows:
        cols = tr.findAll('td')

        company, symbolId = parse_company(cols[1].find('a'))
        item = {
            'symbol': cols[0].string,
            'company': company,
            'isin': symbolId,
            'currency': cols[2].string,
            'price': cols[3].string.replace(',','')
        }
        data.append(item)
    return data


def fetch_content(index_label, base_url):
    with requests.Session() as s:
        content, last_page = parse_first_page(base_url, s)
        logger.info('Fetching index %s components; %s pages' % (index_label, last_page))
        sleep(SCRAPE_WAIT_SECS)
        for page in [i+1 for i in range(1, last_page)]:
            content_url = base_url + "&page={}".format(page)
            try:
                soup = fetch_page(content_url, s)
                page_content = parse_table(soup)
                content.extend(page_content)
                sleep(SCRAPE_WAIT_SECS)
            except:
                write_content_to_csv(content, index_label, page)
                logger.exception('PAGE LOAD FAILURE')

        return content


def convert_content_to_dataframe(content):
    return (
        pd.DataFrame(content)
        .assign(price = lambda x: pd.to_numeric(x.price, errors='coerce'))
        .sort_values(by=['company'])
        [['symbol', 'company', 'isin', 'currency', 'price']]
    )


def write_content_to_csv(content, index_label, page):
    with open(utils.get_raw_file('{}-partial-page-upto-{}.csv'.format(index_label, page)), 'w') as file:
        for item in content:
            file.write('"{}","{}","{}","{}","{}"\n'.format(item['symbol'],item['company'],item['isin'],item['currency'],item['price']))


CONSTITUENTS_BASE_URL = "https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/indices/summary/summary-indices-constituents.html?index="

def scrape_index_constituents(index_label, index_name):
    url = CONSTITUENTS_BASE_URL + index_name
    content = fetch_content(index_label, url)
    df = convert_content_to_dataframe(content)
    filename = '%s_components.csv' % index_label
    logger.info('Saving raw output to %s' % filename)
    df.to_csv(utils.get_raw_file(filename), index=False)
    return df


def scrape_aim100():
    scrape_index_constituents('aim100', 'AIM1')


def scrape_ftse_all_share():
    scrape_index_constituents('ftse_allshare', 'ASX')


def scrape_ftse_aim_all_share():
    scrape_index_constituents('ftse_aim_allshare', 'AXX')


def scrape_ftse_smallcap():
    url = "https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/indices/summary/summary-techmarkindices-constituents.html?index=SMX"
    content = fetch_content('ftse_smallcap', url)
    df = convert_content_to_dataframe(content)
    df.to_csv('ftse_small_cap_components.csv', index=False)
