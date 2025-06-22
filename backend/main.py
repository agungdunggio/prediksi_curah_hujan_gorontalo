from fastapi import FastAPI
from lstm_api.schemas.request_model import InputData
from lstm_api.utils.predict import predict_lstm

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to LSTM Prediction API!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello from FastAPI!"}

@app.post("/predict")
def predict(input: InputData):
    result = predict_lstm(input.data)
    return {"prediction": result}
