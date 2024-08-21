from typing import Any, Dict, Optional
from nextmatter.endpoint_validator import EndpointValidator

class FormField:
    def __init__(self, api, id: str, name: str, type: str, required: bool, options: Optional[Dict[str, Any]] = None, **kwargs):
        self.api = api
        self.id = id
        self.name = name
        self.type = type
        self.required = required
        self.options = options
        self.attributes = kwargs

    def get_form_field_detail(self, workflow_id: str, step_id: str, form_field_id: str) -> Dict[str, Any]:
        validator = EndpointValidator('detail_of_form_field')
        request_data = validator.make_request(path_params={"workflow_id": workflow_id, "step_id": step_id, "form_field_id": form_field_id})
        response = self.api.session.get(request_data['url'], headers=self.api.headers)
        return response.json()