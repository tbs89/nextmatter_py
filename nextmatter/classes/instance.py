from typing import Any, Dict, List, Optional
from nextmatter.exceptions import InvalidPageSizeException
from nextmatter.endpoint_validator import EndpointValidator

class Instance:
    VALID_QUERY_PARAMS = [
        "name", "process", "deadline", "priority", "tags", "step_assignments"
    ]
    
    VALID_BODY_PARAMS = [
        "name", "process", "deadline", "priority", "tags", "step_assignments"
    ]
    
    VALID_PATH_PARAMS = [
        "id"
    ]

    def __init__(self, api, id: str, name: str, process: str, deadline: Optional[str] = None, priority: Optional[str] = None, **kwargs):
        self.api = api
        self.id = id
        self.name = name
        self.process = process
        self.deadline = deadline
        self.priority = priority
        self.attributes = kwargs

    def create_instance(self, data: Dict[str, Any]) -> Dict[str, Any]:
        validator = EndpointValidator('create_instance')
        request_data = validator.make_request(body_params=data)
        response = self.api.session.post(request_data['url'], headers=self.api.headers, json=request_data['body_params'])
        return response.json()

    def delete_instances(self, instance_ids: List[str]) -> Dict[str, Any]:
        validator = EndpointValidator('delete_instances')
        request_data = validator.make_request(body_params={"ids": instance_ids})
        response = self.api.session.delete(request_data['url'], headers=self.api.headers, json=request_data['body_params'])
        return response.json()

    def stop_instances(self, instance_ids: List[str]) -> Dict[str, Any]:
        validator = EndpointValidator('stop_instances')
        request_data = validator.make_request(body_params={"ids": instance_ids})
        response = self.api.session.post(request_data['url'], headers=self.api.headers, json=request_data['body_params'])
        return response.json()

    def delete_instances_post(self, instance_ids: List[str]) -> Dict[str, Any]:
        validator = EndpointValidator('delete_instances_post')
        request_data = validator.make_request(body_params={"ids": instance_ids})
        response = self.api.session.post(request_data['url'], headers=self.api.headers, json=request_data['body_params'])
        return response.json()

    def get_instance(self, instance_id: str, **query_params) -> Dict[str, Any]:
        validator = EndpointValidator('get_instance')
        request_data = validator.make_request(query_params=query_params, path_params={"id": instance_id})
        response = self.api.session.get(request_data['url'], headers=self.api.headers, params=request_data['query_params'])
        return response.json()

    def update_instance(self, instance_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        validator = EndpointValidator('update_instance')
        request_data = validator.make_request(body_params=data, path_params={"id": instance_id})
        response = self.api.session.put(request_data['url'], headers=self.api.headers, json=request_data['body_params'])
        return response.json()

    def partially_update_instance(self, instance_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        validator = EndpointValidator('partially_update_instance')
        request_data = validator.make_request(body_params=data, path_params={"id": instance_id})
        response = self.api.session.patch(request_data['url'], headers=self.api.headers, json=request_data['body_params'])
        return response.json()

    def complete_step(self, instance_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        validator = EndpointValidator('complete_step')
        request_data = validator.make_request(body_params=data, path_params={"id": instance_id})
        response = self.api.session.post(request_data['url'], headers=self.api.headers, json=request_data['body_params'])
        return response.json()

    def list_instances(self, page: int = 1, page_size: int = 100, **query_params) -> List[Dict[str, Any]]:
        if page_size > 500:
            raise InvalidPageSizeException(page_size)
        query_params.update({"page": page, "page_size": page_size})
        validator = EndpointValidator('list_instances')
        request_data = validator.make_request(query_params=query_params)
        response = self.api.session.get(request_data['url'], headers=self.api.headers, params=request_data['query_params'])
        return response.json()