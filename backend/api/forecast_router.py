from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime, timedelta, timezone

from models.schemas import (
    PredictionRequest, 
    DataAdditionRequest, 
    PredictionResponse, 
    BufferStatusResponse,
    DataAdditionResponse,
    PredictionPoint,
    PredictionData
)
from services.prediction_service import prediction_service
from core.config import settings
from core.security import get_api_key

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse, summary="Prediksi time series ke depan")
def predict(data: PredictionRequest):
    raw_predictions = prediction_service.predict(n_days=data.n_days)
    
    if raw_predictions is None:
        raise HTTPException(
            status_code=400,
            detail=f"Not enough data. Need {prediction_service.get_buffer_status()['needed']} more data points."
        )

    start_time = datetime.now(timezone.utc)
    prediction_points = [
        PredictionPoint(date=(start_time + timedelta(days=i)).date(), value=val)
        for i, val in enumerate(raw_predictions)
    ]
    
    response_data = PredictionData(
        location="Gorontalo",
        unit="mm/hari",
        model_used=f"lstm-v{settings.TIME_STEP}",
        prediction_start=prediction_points[0].date,
        prediction_end=prediction_points[-1].date,
        predictions=prediction_points
    )

    return PredictionResponse(
        message="Prediksi curah hujan berhasil diambil",
        data=[response_data]
    )


@router.post("/add-data", response_model=DataAdditionResponse, summary="Tambah data untuk buffer", status_code=201)
def add_data(data: DataAdditionRequest, api_key: str = Depends(get_api_key)):
    result_dict = prediction_service.add_data(data.values)
    return DataAdditionResponse(
        message="Data berhasil ditambahkan ke buffer",
        data=result_dict
    )


@router.get("/buffer-status", response_model=BufferStatusResponse, summary="Cek status buffer")
def get_buffer_status(api_key: str = Depends(get_api_key)):
    status_dict = prediction_service.get_buffer_status()
    return BufferStatusResponse(
        message="Status buffer berhasil diambil",
        data=status_dict
    )