'''TODO:
IMPORT ML MODEL
POST PREDICTIONS BACK TO THE MONGODB
'''
import asyncio
from datetime import datetime, timedelta
from ...backend.db.mongo_util import MongoDBUtil
from typing import List, Tuple, Union
from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from fastapi import FastAPI
from examples.example import run_example
from backend.time_series import time_series_example

uri = os.getenv("MONGO_URI")
app = FastAPI()
db = MongoDBUtil()



@app.on_event("startup")
async def startup_db_client(uri):
    client = MongoDBUtil(uri)
    client.init_db("MassDebaters", "snow-forecast")
    
    

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()

#Endpoints
@app.get("/snow_data")
async def get_snow_data(start_date:datetime, end_date:datetime, location:List):
    out = await time_series_example(location, start_date, end_date)
    return out

    

#ML COMPONENT
@app.websocket("/predict")
async def predict(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        prediction_input = PredictionInput(**data)
        prediction = ml_model.predict(prediction_input.dict())  # Replace with your prediction logic
        await websocket.send_json({"prediction": prediction})
