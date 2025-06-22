from pydantic import BaseModel
from typing import List

class InputData(BaseModel):
    data: List[float]
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "data": [100.5, 120.3, 95.7, 110.2, 130.1]
            }
        }
    }
