import pandas as pd
import numpy as np
import string

from helpers import utils
from app import symbols


logger = utils.get_logger(__name__)


def scrape_lse_full():
    base_url = "https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/prices-search/stock-prices-search.html?initial="
    
    master = symbols.fetch_content('all', base_url + "0")
    write_content_to_csv(master, '0')
    
    for alpha_index in list(string.ascii_uppercase):
        try:
            content = symbols.fetch_content('all', base_url + alpha_index)
            write_content_to_csv(content, alpha_index)
            master.extend(content)
        except:
            logger.exception('SCRAPE FAILURE')
            return master
    
    return master


def write_content_to_csv(content, alpha_index):
    with open(utils.get_raw_file('lse-full-scrape-{}.csv'.format(alpha_index)), 'w') as file:
        for item in content:
            file.write('"{}","{}","{}","{}","{}"\n'.format(item['company'],item['currency'],item['price'],item['symbol'],item['isin']))


if __name__ == "__main__":
    content = scrape_lse_full()

    try:
        df = symbols.convert_content_to_dataframe(content)
        df.to_csv(utils.get_raw_file('lse_all_components.csv'), index=False)
    except:
        logger.exception('DF FAILURE')
