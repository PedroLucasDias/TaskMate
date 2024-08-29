from json import loads, dumps
from copy import deepcopy
from typing import Dict, Any

from utils.validate.json import validate

class BaseModel:
    def __init__(self):
        self._data: Dict[str, Any] = {}

    def load_json(self, json_data: str):
        if not isinstance(json_data, str):
            raise ValueError("json_data deve ser uma string")

        data = loads(json_data)
        self._data = validate(data)

    def to_json(self) -> str:
        return dumps(self._data)

    def load_dict(self, data: dict):
        self._data = validate(data)

    def to_dict(self) -> dict:
        return deepcopy(self._data)
