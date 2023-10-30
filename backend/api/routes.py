'''TODO:
IMPORT ML MODEL
POST PREDICTIONS BACK TO THE MONGODB
'''

from datetime import datetime, timedelta
from ..db.mongo_util import db_util
from typing import List, Tuple, Union
from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from fastapi import FastAPI
from examples.example import run_example
from backend.time_series import time_series_example

app = FastAPI()
db = db_util()



@app.on_event("startup")
async def startup_db_client(uri):
    global client
    client = AsyncIOMotorClient(uri)
    # Or use any URL you need

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
