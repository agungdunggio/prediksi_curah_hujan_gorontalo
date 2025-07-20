import numpy as np
import json
import os
from collections import deque
from datetime import datetime, timedelta
from tensorflow.keras.models import load_model
from typing import List

from core.config import settings 

class PredictionService:
    def __init__(self):
        self.model = load_model(settings.MODEL_PATH)
        self.data_buffer = self._load_data_buffer()
        print("Prediction Service Initialized: Model and Buffer Loaded.")

    def _load_data_buffer(self) -> dict:
        if os.path.exists(settings.DATA_BUFFER_PATH):
            try:
                with open(settings.DATA_BUFFER_PATH, 'r') as f:
                    data = json.load(f)
                    # Jika data buffer lama (list), konversi ke dict
                    if isinstance(data, list):
                        return {"buffer": data, "updated_at": None}
                    return data
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load buffer file. Creating a new one. Error: {e}")
        return {"buffer": [], "updated_at": None}

    def _save_data_buffer(self):
        buffer_dir = os.path.dirname(settings.DATA_BUFFER_PATH)
        os.makedirs(buffer_dir, exist_ok=True)
        with open(settings.DATA_BUFFER_PATH, 'w') as f:
            json.dump(self.data_buffer, f)
            
    def add_data(self, values: List) -> dict:
        new_buffer = []

        # Jika values adalah list of dict (format baru)
        if values and isinstance(values[0], dict) and 'date' in values[0] and 'value' in values[0]:
            for entry in values:
                new_buffer.append({
                    "date": entry["date"],
                    "value": entry["value"]
                })
        else:
            # Fallback: list of float
            start_date = datetime.now()
            for i, value in enumerate(values):
                entry = {
                    "date": (start_date + timedelta(days=i)).strftime("%Y-%m-%d"),
                    "value": value
                }
                new_buffer.append(entry)

        # Potong agar hanya simpan TIME_STEP terakhir
        new_buffer = new_buffer[-settings.TIME_STEP:]

        self.data_buffer["buffer"] = new_buffer
        self.data_buffer["updated_at"] = datetime.now().isoformat()
        self._save_data_buffer()

        return {
            "message": f"Buffer overwritten with {len(new_buffer)} data points",
            "buffer_size": len(new_buffer),
            "needed": max(0, settings.TIME_STEP - len(new_buffer)),
            "updated_at": self.data_buffer["updated_at"]
        }
        
    def get_buffer_status(self) -> dict:
        return {
            "current_size": len(self.data_buffer["buffer"]),
            "needed": max(0, settings.TIME_STEP - len(self.data_buffer["buffer"])),
            "current_data": list(self.data_buffer["buffer"]),
            "updated_at": self.data_buffer["updated_at"]
        }

    def predict(self, n_days: int) -> List[dict]:
        # Ambil hanya data sebelum hari ini, urutkan berdasarkan tanggal
        today = datetime.now().date()
        filtered = [item for item in self.data_buffer["buffer"] if datetime.strptime(item['date'], "%Y-%m-%d").date() < today]
        # Urutkan ascending by date
        filtered.sort(key=lambda x: x['date'])
        # Ambil 15 data terakhir
        history = [item['value'] for item in filtered[-settings.TIME_STEP:]]
        if len(history) < settings.TIME_STEP:
            return []
        predictions = []
        # Tentukan tanggal mulai prediksi (hari terakhir di history)
        last_date = datetime.strptime(filtered[-1]['date'], "%Y-%m-%d")
        for i in range(n_days):
            input_seq = np.array(history[-settings.TIME_STEP:]).reshape((1, settings.TIME_STEP, 1))
            next_pred = self.model.predict(input_seq, verbose=0)[0][0]
            pred_date = (last_date + timedelta(days=i+1)).strftime("%Y-%m-%d")
            predictions.append({"date": pred_date, "value": float(next_pred)})
            history.append(next_pred)
        return predictions

# Buat satu instance service yang akan digunakan oleh seluruh aplikasi (singleton pattern)
prediction_service = PredictionService()