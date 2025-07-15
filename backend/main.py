# main.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from api.forecast_router import router as forecast_router

app = FastAPI(
    title="LSTM Time Series Forecast API (Structured)",
    description="A well-structured API for time series forecasting.",
    version="2.0.0"
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Handler ini akan menangkap semua HTTPException dan memformat ulang
    responsnya agar sesuai dengan struktur BaseAPIResponse kita.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": False,
            "message": exc.detail,
        },
    )

# Sertakan router ke aplikasi utama
app.include_router(forecast_router, prefix="/api/v1", tags=["Forecasting"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the LSTM Forecast API. Go to /docs for documentation."}