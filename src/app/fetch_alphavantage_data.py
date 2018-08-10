import pandas as pd
import numpy as np
import requests
import os.path
from time import sleep

from helpers import utils, config

logger = utils.get_logger(__name__)

HOLDOFF_TIMER = 12
DAILY_ADJUSTED_BASE = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize=full&apikey={}&datatype=csv"
FOREX_BASE = "https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={}&to_symbol={}&outputsize=full&apikey={}&datatype=csv"

credentials = config.read_credentials('alphavantage')


def download_adj_daily_prices(symbols):
    load_failures = []

    with requests.Session() as s:
        for idx, symbol in enumerate(symbols):
            lse_symbol = symbol + '.L'
            output_filename = '%s.csv' % symbol
            output_path = utils.get_project_path('data', 'raw', 'symbol_prices', output_filename)
            
            if os.path.exists(output_path):
                logger.info('Skipping %s; already exists' % symbol)
                continue

            if idx > 0:
                sleep(HOLDOFF_TIMER)
            
            try:
                logger.info('Fetching %s' % lse_symbol)
                with s.get(DAILY_ADJUSTED_BASE.format(lse_symbol, credentials['apikey']), stream=True) as r:
                    if r.status_code == 200:
                        with open(output_path, 'wb') as fd:
                            for chunk in r.iter_content(chunk_size=128):
                                fd.write(chunk)
                        logger.info('Saved %s' % output_filename)
                    else:
                        load_failures.append(symbol)
            except:
                load_failures.append(symbol)
                logger.exception('LOAD FAILURE for %s' % symbol)

    if len(load_failures) > 0:
        logger.info('Failed to download: %s' % load_failures)


def get_symbols(filepath):
    return (
        pd.read_csv(filepath)
        .assign(symbol = lambda x: x.symbol.str.rstrip('.'))
        .symbol
        .unique()
    )


def fetch_aim100_symbols():
    symbols = get_symbols(utils.get_raw_file('aim100_components-20180808.csv'))
    download_adj_daily_prices(symbols)


def fetch_ftse_smallcap_symbols():
    symbols = get_symbols(utils.get_raw_file('ftse_smallcap_components-20180808.csv'))
    download_adj_daily_prices(symbols)


def fetch_ftse_allshare_symbols():
    symbols = get_symbols(utils.get_raw_file('ftse_allshare_components-20180809.csv'))
    download_adj_daily_prices(symbols)


def fetch_ftse_aim_allshare_symbols():
    symbols = get_symbols(utils.get_raw_file('ftse_aim_allshare_components-20180809.csv'))
    download_adj_daily_prices(symbols)


def fetch_adhoc_symbols():
    symbols = [ 'AO', 'AST', 'CGH', 'CNKS', 'DRG', 'FA', 'HW', 'LION', 'PET', 'SHED', 'ULE', 'YU', 'ARG', 'BT.A', 'CHA', 'CRH', 'DX.', 'GSH', 'KIN', 'NGR', 'SGZ', 'UJO', 'VP', 'ZMNO' ]
    download_adj_daily_prices(symbols)


def download_forex(currencies):
    load_failures = []

    currency_pairs = [item for sublist in [[(x, 'GBP'), ('GBP', x)] for x in currencies] for item in sublist]

    with requests.Session() as s:
        for idx, (from_currency, to_currency) in enumerate(currency_pairs):
            currency_pair = '%s-%s' % (from_currency, to_currency)
            output_filename = '%s.csv' % currency_pair
            output_path = utils.get_project_path('data', 'raw', 'forex', output_filename)

            if os.path.exists(output_path):
                logger.info('Skipping %s; already exists' % currency_pair)
                continue

            if idx > 0:
                sleep(HOLDOFF_TIMER)

            try:
                logger.info('Fetching %s' % currency_pair)
                with s.get(FOREX_BASE.format(from_currency, to_currency, credentials['apikey'])) as r:
                    if r.status_code != 200:
                        raise ValueError("API CALL FAILURE for %s" % currency_pair)

                    if any(s in r.text.lower() for s in ('information', 'error')) and "alphavantage.co" in r.text.lower():
                        raise ValueError("INVALID RESPONSE for %s" % currency_pair)

                    with open(output_path, 'wb') as file:
                        logger.info('Writing content to %s' % output_filename)
                        file.write(r.content)
            except:
                load_failures.append(currency_pair)
                logger.exception('API FAILURE for %s' % currency_pair)
                
    if len(load_failures) > 0:
        logger.info('FAILURES: %s' % load_failures)


def get_currencies():
    return sorted(
        pd.read_csv(utils.get_raw_file('lse_all_components-20180808.csv'), low_memory=False)
        .loc[lambda x: ~x.currency.isin(['GBP','GBX'])]
        .currency
        .unique()
    )


def fetch_forex():
    currencies = get_currencies()
    download_forex(currencies)


if __name__ == "__main__":
    fetch_adhoc_symbols()
