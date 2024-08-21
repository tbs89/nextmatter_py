from typing import Any, Dict, Optional
from nextmatter.endpoint_validator import EndpointValidator

class Image:
    def __init__(self, api, created_time: str, process: Optional[int] = None, process_instance: Optional[int] = None, image_uri: Optional[str] = None):
        self.api = api
        self.created_time = created_time
        self.process = process
        self.process_instance = process_instance
        self.image_uri = image_uri

    def upload_image(self, image_path: str) -> Dict[str, Any]:
        validator = EndpointValidator('upload_image')
        request_data = validator.make_request()
        with open(image_path, 'rb') as image:
            response = self.api.session.post(request_data['url'], headers=self.api.headers, files={'image': image})
        return response.json()