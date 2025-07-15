import numpy as np
import json
import os
from collections import deque
from tensorflow.keras.models import load_model
from typing import List

from core.config import settings # Impor konfigurasi

class PredictionService:
    def __init__(self):
        self.model = load_model(settings.MODEL_PATH)
        self.data_buffer = self._load_data_buffer()
        print("Prediction Service Initialized: Model and Buffer Loaded.")

    def _load_data_buffer(self) -> deque:
        if os.path.exists(settings.DATA_BUFFER_PATH):
            try:
                with open(settings.DATA_BUFFER_PATH, 'r') as f:
                    data = json.load(f)
                    return deque(data, maxlen=settings.TIME_STEP)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load buffer file. Creating a new one. Error: {e}")
        return deque(maxlen=settings.TIME_STEP)

    def _save_data_buffer(self):
        buffer_dir = os.path.dirname(settings.DATA_BUFFER_PATH)
        os.makedirs(buffer_dir, exist_ok=True)
        with open(settings.DATA_BUFFER_PATH, 'w') as f:
            json.dump(list(self.data_buffer), f)
            
    def add_data(self, values: List[float]) -> dict:
        for value in values:
            self.data_buffer.append(value)
        self._save_data_buffer()
        return {
            "message": f"Added {len(values)} data points",
            "buffer_size": len(self.data_buffer),
            "needed": max(0, settings.TIME_STEP - len(self.data_buffer))
        }
        
    def get_buffer_status(self) -> dict:
        return {
            "current_size": len(self.data_buffer),
            "needed": max(0, settings.TIME_STEP - len(self.data_buffer)),
            "current_data": list(self.data_buffer)
        }

    def predict(self, n_days: int) -> List[float]:
        if len(self.data_buffer) < settings.TIME_STEP:
            return None # Akan ditangani di layer API

        history = list(self.data_buffer)
        predictions = []

        for _ in range(n_days):
            input_seq = np.array(history[-settings.TIME_STEP:]).reshape((1, settings.TIME_STEP, 1))
            next_pred = self.model.predict(input_seq, verbose=0)[0][0]
            predictions.append(float(next_pred))
            history.append(next_pred)

        return predictions

# Buat satu instance service yang akan digunakan oleh seluruh aplikasi (singleton pattern)
prediction_service = PredictionService()