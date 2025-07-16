from pydantic import BaseModel
from typing import List, Dict, Any
from datetime import date

class PredictionRequest(BaseModel):
    n_days: int = 1

class DataAdditionRequest(BaseModel):
    values: List[float]

class BaseAPIResponse(BaseModel):
    status: bool = True
    message: str

class PredictionPoint(BaseModel):
    date: date
    value: float

class PredictionData(BaseModel):
    location: str
    unit: str
    model_used: str
    prediction_start: date
    prediction_end: date
    predictions: List[PredictionPoint]

class PredictionResponse(BaseAPIResponse):
    data: List[PredictionData]

class BufferData(BaseModel):
    current_size: int
    needed: int
    current_data: List[float]

class BufferStatusResponse(BaseAPIResponse):
    data: BufferData
    
class DataAdditionResponse(BaseAPIResponse):
    data: Dict[str, Any]