from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.post("/predict")
async def predict(data: dict):
    prediction = np.random.choice([0,1])
    return {"prediction": int(prediction)}