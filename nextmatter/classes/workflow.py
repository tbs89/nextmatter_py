from typing import Any, Dict, List, Optional
from nextmatter.endpoint_validator import EndpointValidator

class Workflow:
    def __init__(self, api, id: str, name: str, created_at: str, updated_at: str, **kwargs):
        self.api = api
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.attributes = kwargs

    def list_workflows(self) -> List[Dict[str, Any]]:
        validator = EndpointValidator('list_workflows')
        request_data = validator.make_request()
        response = self.api.session.get(request_data['url'], headers=self.api.headers)
        return response.json()

    def get_workflow(self, workflow_id: str) -> Dict[str, Any]:
        validator = EndpointValidator('get_workflow')
        request_data = validator.make_request(path_params={"id": workflow_id})
        response = self.api.session.get(request_data['url'], headers=self.api.headers)
        return response.json()