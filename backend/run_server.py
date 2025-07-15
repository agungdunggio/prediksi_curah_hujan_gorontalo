#!/usr/bin/env python3
"""
Script untuk menjalankan server FastAPI
"""

import uvicorn
import os
import sys

def main():
    if not os.path.exists('main.py'):
        print("❌ Error: main.py tidak ditemukan. Pastikan Anda menjalankan script ini dari direktori backend/")
        sys.exit(1)
    
    if not os.path.exists('./models/model_LSTM_beta.h5'):
        print("⚠️  Warning: Model file './models/model_LSTM_beta.h5' tidak ditemukan")
        print("   Pastikan model sudah ada sebelum menggunakan endpoint /predict")
    
    print("🚀 Starting FastAPI server...")
    print("📡 Server akan berjalan di: http://localhost:8000")
    print("📚 API docs akan tersedia di: http://localhost:8000/docs")
    print("🔄 Tekan Ctrl+C untuk menghentikan server")
    print()
    
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main() 