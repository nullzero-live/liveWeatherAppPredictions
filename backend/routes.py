from fastapi import FastAPI
from server_logs.logger_util import setup_logger
import meteomatics
import json
from utils.exceptions import API_EXCEPTIONS







serv_logs = setup_logger("snow_app")
app = FastAPI()

@app.get("/")
async def root():
    try:
        serv_logs.info("Getting Data....")
        snow_results = mtnhubsnow.snow_data(
        publisher='all',
        obs_type='snow_conditions,snowpack_test',
        limit=1000,
        start=None,
        end=None,
        bbox=None,
        filter=True)
    except Exception as e:
        serv_logs.error(e)
    return {"results":snow_results}

