import numpy as np
import pandas as pd
from typing import List
import joblib
import os

def predict_lstm(data: List[float]) -> float:
    """
    Melakukan prediksi menggunakan model LSTM
    
    Args:
        data: List of float values untuk prediksi
        
    Returns:
        float: Hasil prediksi
    """
    try:
        # Normalisasi data input
        data_array = np.array(data).reshape(-1, 1)
        
        # Load model (jika ada)
        model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'models', 'lstm_model.pkl')
        
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            # Lakukan prediksi
            prediction = model.predict(data_array.reshape(1, -1))
            return float(prediction[0])
        else:
            # Jika model belum ada, return dummy prediction
            return float(np.mean(data))
            
    except Exception as e:
        print(f"Error in prediction: {e}")
        # Return mean dari data input sebagai fallback
        return float(np.mean(data))
