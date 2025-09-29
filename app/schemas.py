from pydantic import BaseModel, ValidationError, root_validator
from typing import List, Dict, Any

class PredictItem(BaseModel):
    # aceptamos un dict con feature_name: value
    __root__: Dict[str, float]

    @root_validator(pre=True)
    def ensure_numeric(cls, values):
        # values may be like {'feature1': 1.0, ...}
        if not isinstance(values, dict):
            raise ValueError("Payload for a single record must be a JSON object with features")
        return values

class PredictRequest(BaseModel):
    instances: List[PredictItem]
