import pandas as pd
import numpy as np
from datetime import date as dt

from helpers import utils
from app import company_files as company

logger = utils.get_logger(__name__)


colOrder = ['loaddate', 'listdate', 'market', 'company', 'sector', 'subsector', 'marketcap', 'country']


def load_excel_sheet(load_date, load_definition, sheet_idx, sheet_definition):
    return (
        pd.read_excel(utils.get_project_path('data', 'external', 'company-files', load_definition['filename']),
                    sheet_name=sheet_idx, header=None, names=sheet_definition['colNames'],
                    usecols=sheet_definition['parseCols'], skiprows=sheet_definition['headerRow'])
        .assign(loaddate = pd.to_datetime(load_date))
        [colOrder]
    )


def load_all():
    data = []
    missed_sheets = []

    for load_def in company.files:
        for idx, sheet in enumerate(load_def['sheets']):
            load_date = dt(load_def['year'], idx+1, 1)
            logger.info('Loading %s' % load_date.strftime('%Y-%B'))
            try:
                data.append(load_excel_sheet(load_date, load_def, idx, sheet))
            except:
                missed_sheets.append(load_date.strftime('%Y-%B'))
                logger.exception('LOAD SHEET FAIL')

    if len(missed_sheets) > 0:
        logger.info('Missing: %s' % missed_sheets)

    if len(data) > 0:
        df = pd.concat(data)
        filename = 'company_files_all.csv'
        logger.info('Writing raw output file %s' % filename)
        df.to_csv(utils.get_raw_file(filename), index=False)

    return df


if __name__ == "__main__":
    load_all()
