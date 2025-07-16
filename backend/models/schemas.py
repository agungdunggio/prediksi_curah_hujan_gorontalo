from pydantic import BaseModel, model_validator
from typing import List, Dict, Any
from datetime import date, timedelta

class PredictionRequest(BaseModel):
    n_days: int = 1

class DataAdditionRequest(BaseModel):
    data_start: date
    data_end: date
    values: List[float]

    @model_validator(mode='after')
    def check_values_length(self):
        n_days = (self.data_end - self.data_start).days + 1
        if len(self.values) != n_days:
            raise ValueError(f"Length of values ({len(self.values)}) must match number of days between data_start and data_end ({n_days})")
        return self

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
    current_data: List[Dict[str, Any]]

class BufferStatusResponse(BaseAPIResponse):
    data: BufferData
    
class DataAdditionResponse(BaseAPIResponse):
    data: Dict[str, Any]