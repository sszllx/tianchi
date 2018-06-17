import os
import pandas as pd

from keras.utils import get_file


BASE_URL = "https://github.com/suzg/fddc2018-01-data/releases/download/20180529/"
THIS_DIR = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
MD5_FILE = os.path.abspath(os.path.join(THIS_DIR, '../data/md5-gz.txt'))

CSV_OPTS = {
    'MarketData.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['END_DATE']),
    'BalanceSheet-Bank.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['PUBLISH_DATE', 'END_DATE_REP', 'END_DATE']),
    'BalanceSheet-GeneralBusiness.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['PUBLISH_DATE', 'END_DATE_REP', 'END_DATE']),
    'BalanceSheet-Insurance.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['PUBLISH_DATE', 'END_DATE_REP', 'END_DATE']),
    'BalanceSheet-Securities.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['PUBLISH_DATE', 'END_DATE_REP', 'END_DATE']),
    'CashFlowStatement-Bank.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['PUBLISH_DATE', 'END_DATE_REP', 'END_DATE']),
    'CashFlowStatement-GeneralBusiness.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['PUBLISH_DATE', 'END_DATE_REP', 'END_DATE']),
    'CashFlowStatement-Insurance.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['PUBLISH_DATE', 'END_DATE_REP', 'END_DATE']),
    'CashFlowStatement-Securities.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['PUBLISH_DATE', 'END_DATE_REP', 'END_DATE']),
    'IncomeStatement-Bank.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['PUBLISH_DATE', 'END_DATE_REP', 'END_DATE']),
    'IncomeStatement-GeneralBusiness.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['PUBLISH_DATE', 'END_DATE_REP', 'END_DATE']),
    'IncomeStatement-Insurance.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['PUBLISH_DATE', 'END_DATE_REP', 'END_DATE']),
    'IncomeStatement-Securities.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['PUBLISH_DATE', 'END_DATE_REP', 'END_DATE']),
    'CompanyOperation.csv':
        dict(dtype={"TICKER_SYMBOL":str}, parse_dates=['END_DATE']),
    'MacroIndustry.csv':
        dict(parse_dates=['PERIOD_DATE']),
}

def get_files():
    FILES = {}
    with open(MD5_FILE) as f:
        for line in f:
            line = line.strip()
            parts = line.split(' ')
            md5 = parts[0]
            fname = parts[-1]
            localname = fname.replace('.tar.gz', '.csv')
            url = BASE_URL + fname
            FILES[localname] = get_file(localname, url, cache_subdir='fddc2018-01', untar=True, file_hash=md5)

    return FILES

def read_file(filename):
    FILES = get_files()
    opts = CSV_OPTS[filename]
    df = pd.read_csv(FILES[filename], **opts)
    
    return df
