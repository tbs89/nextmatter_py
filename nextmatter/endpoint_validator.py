from typing import Any, Dict
from pydantic import BaseModel, Field, ValidationError
from nextmatter.exceptions import InvalidQueryParamException, InvalidParamFormatException
import json
from dateutil.parser import parse
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
tools_dir = os.path.join(current_dir, '..', 'tools')
endpoint_params_path = os.path.join(tools_dir, 'endpoint_params.json')

with open(endpoint_params_path) as f:
    ENDPOINT_PARAMS = json.load(f)

class EndpointValidator:
    def __init__(self, endpoint_name: str):
        self.endpoint_name = endpoint_name
        self.endpoint_config = ENDPOINT_PARAMS.get(endpoint_name)
        if not self.endpoint_config:
            raise ValueError(f"Endpoint '{endpoint_name}' not found in configuration.")

    def validate_params(self, params: Dict[str, Any], param_type: str):
        valid_params = self.endpoint_config.get(param_type, {})
        for param, value in params.items():
            if param not in valid_params:
                raise InvalidQueryParamException(param, list(valid_params.keys()))
            expected_format = valid_params[param]
            if not self._validate_format(value, expected_format):
                raise InvalidParamFormatException(param, expected_format)

    def _validate_format(self, value: Any, expected_format: str) -> bool:
        if expected_format == "string" and isinstance(value, str):
            return True
        if expected_format == "integer" and isinstance(value, int):
            return True
        if expected_format == "date-time" and isinstance(value, str): 
            try:
                parse(value)
                return True
            except ValueError:
                return False
        if expected_format.startswith("array") and isinstance(value, list):
            return True
        if expected_format == "boolean" and isinstance(value, bool):
            return True
        return False

    def build_url(self, path_params: Dict[str, Any]) -> str:
        url = self.endpoint_config['url']
        for param, value in path_params.items():
            url = url.replace(f"{{{param}}}", str(value))
        return url

    def make_request(self, body_params: Dict[str, Any] = {}, query_params: Dict[str, Any] = {}, path_params: Dict[str, Any] = {}):
        self.validate_params(body_params, 'body_params')
        self.validate_params(query_params, 'query_params')
        self.validate_params(path_params, 'path_params')
        url = self.build_url(path_params)
        method = self.endpoint_config['method']
        return {
            "method": method,
            "url": url,
            "body_params": body_params,
            "query_params": query_params
        }