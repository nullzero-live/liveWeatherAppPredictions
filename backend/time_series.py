
import argparse
import datetime as dt
import logging
import sys
from utils.exceptions import API_EXCEPTIONS
from utils.credentials import username as username_default, password as password_default
from utils._constants_ import LOGGERNAME, API_BASE_URL
from examples.example import run_example
import api as api
from utils.parameters import *



def time_series_example(username: str = username_default, password: str = password_default, _logger):
    _logger.info("\ntime series:")
    param_columns = [param_colums.append(parameter) for parameter in PARAMETERS_TS]
    try:
        df_ts = api.query_time_series(coordinate_list=COORDINATES_TS, startdate=STARTDATE_TS, enddate=ENDDATE_TS, 
                                      interval=INTERVAL_TS, parameters=PARAMETERS_TS, username=username_default, password=password_default,  
                                        api_base_url=API_BASE_URL) 
                              

        _logger.info("Dataframe head \n" + df_ts.head().to_string())
    except Exception as e:
        _logger.error("Failed, the exception is {}".format(e), exc_info=True)
        return False
    return df_ts.to_csv(path=f"../logs/{STARTDATE_TS}.csv", columns=param_columns, header=True, encoding='utf-8',)