# /core/security.py
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from core.config import settings

# Mendefinisikan skema API Key, yaitu akan dicari di header "X-API-Key"
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def get_api_key(api_key: str = Security(api_key_header)):
    """
    Fungsi dependency yang akan dijalankan di setiap request.
    Memeriksa apakah API Key yang diberikan valid.
    """
    if api_key == settings.API_KEY:
        return api_key
    else:
        # Jika tidak valid, kirim error 403 Forbidden
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Anda Tidak Memiliki Akses Ke Endpoint Ini"
        )