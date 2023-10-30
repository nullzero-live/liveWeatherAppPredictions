'''TODO:
IMPORT ML MODEL
POST PREDICTIONS BACK TO THE MONGODB
'''
import asyncio
from datetime import datetime, timedelta
from ..backend.db.mongo_util import MongoDBUtil
from typing import List, Tuple, Union
from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from fastapi import FastAPI
from examples.example import run_example
from backend.time_series import time_series_example

uri = os.getenv("MONGO_URI")
app = FastAPI()




@app.on_event("startup")
async def startup_db_client():
    client = MongoDBUtil(db_name="myDB", collection_name="myCollection")
    await client.init_db("MassDebaters", "snow-forecast")
    
    

@app.on_event("shutdown")
async def shutdown_db_client():
    await client.close()

#Endpoints
@app.get("/snow_data")
async def get_snow_data(start_date:datetime, end_date:datetime, location:List):
    out = await time_series_example(location, start_date, end_date)
    return out


#ML COMPONENT
@app.websocket("/predict")
async def predict(websocket: WebSocket):
    await websocket.accept()
    return print(websocket.receive_json())
    '''while True:
        data = await websocket.receive_json()
        prediction_input = PredictionInput(**data)
        prediction = ml_model.predict(prediction_input.dict())  # Replace with your prediction logic
        await websocket.send_json({"prediction": prediction})'''
