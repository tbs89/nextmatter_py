from typing import Any, Dict, Optional
from nextmatter.endpoint_validator import EndpointValidator

class File:
    def __init__(self, api, created_time: str, process: Optional[int] = None, process_instance: Optional[int] = None, file_uri: Optional[str] = None):
        self.api = api
        self.created_time = created_time
        self.process = process
        self.process_instance = process_instance
        self.file_uri = file_uri

    def upload_file(self, file_path: str) -> Dict[str, Any]:
        validator = EndpointValidator('upload_file')
        request_data = validator.make_request()
        with open(file_path, 'rb') as file:
            response = self.api.session.post(request_data['url'], headers=self.api.headers, files={'file': file})
        return response.json()