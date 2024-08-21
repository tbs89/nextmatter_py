ENDPOINTS_PARAMS = {
    "upload_file": {
        "method": "post",
        "url": "https://core.nextmatter.com/api/files/",
        "body_params": {
            "created_time": "date-time",
            "process": "integer",
            "process_instance": "integer"
        },
        "query_params": {},
        "path_params": {}
    },
    "upload_image": {
        "method": "post",
        "url": "https://core.nextmatter.com/api/images/",
        "body_params": {
            "created_time": "date-time",
            "process": "integer",
            "process_instance": "integer"
        },
        "query_params": {},
        "path_params": {}
    },
    "create_instance": {
        "method": "post",
        "url": "https://core.nextmatter.com/api/instances/",
        "body_params": {
            "name": "string",
            "process": "uri",
            "deadline": "date-time",
            "priority": "string",
            "tags": "string",
            "step_assignments": "array"
        },
        "query_params": {},
        "path_params": {}
    },
    "delete_instances": {
        "method": "delete",
        "url": "https://core.nextmatter.com/api/instances/bulk",
        "body_params": {
            "ids": "array[integer]"
        },
        "query_params": {},
        "path_params": {}
    },
    "stop_instances": {
        "method": "post",
        "url": "https://core.nextmatter.com/api/instances/bulk/abort",
        "body_params": {
            "ids": "array[integer]"
        },
        "query_params": {},
        "path_params": {}
    },
    "delete_instances_post": {
        "method": "post",
        "url": "https://core.nextmatter.com/api/instances/bulk/delete",
        "body_params": {
            "ids": "array[integer]"
        },
        "query_params": {},
        "path_params": {}
    },
    "get_instance": {
        "method": "get",
        "url": "https://core.nextmatter.com/api/instances/{id}/",
        "body_params": {},
        "query_params": {
            "inject_values": "boolean",
            "steps_time_frame": "boolean"
        },
        "path_params": {
            "id": "string"
        }
    },
    "update_instance": {
        "method": "put",
        "url": "https://core.nextmatter.com/api/instances/{id}/",
        "body_params": {
            "name": "string",
            "process": "uri",
            "deadline": "date-time",
            "priority": "string",
            "tags": "string",
            "step_assignments": "array"
        },
        "query_params": {},
        "path_params": {
            "id": "string"
        }
    },
    "partially_update_instance": {
        "method": "patch",
        "url": "https://core.nextmatter.com/api/instances/{id}/",
        "body_params": {
            "name": "string",
            "process": "uri",
            "deadline": "date-time",
            "priority": "string",
            "tags": "string",
            "step_assignments": "array"
        },
        "query_params": {},
        "path_params": {
            "id": "string"
        }
    },
    "complete_step": {
        "method": "post",
        "url": "https://core.nextmatter.com/api/instances/{id}/complete_step/",
        "body_params": {
            "step_id": "integer",
            "actions": "array[object]",
            "mode": "string"
        },
        "query_params": {},
        "path_params": {
            "id": "string"
        }
    },
    "list_instances": {
        "method": "get",
        "url": "https://core.nextmatter.com/api/processes/{id}/instances/",
        "body_params": {},
        "query_params": {
            "organization": "string",
            "workflow": "string",
            "progress": "string",
            "id": "number",
            "ordering": "string",
            "status": "string",
            "name": "string",
            "query": "string",
            "priority": "string",
            "started_time": "string",
            "last_updated_time": "string",
            "deadline": "string",
            "step_deadline": "string",
            "aborted_time": "string",
            "completed_time": "string",
            "ended_time": "string",
            "total_runtime_min": "string",
            "total_runtime_max": "string",
            "active_step_id": "string",
            "tags": "string",
            "instance_ids": "string",
            "page": "integer",
            "page_size": "integer"
        },
        "path_params": {
            "id": "string"
        }
    }
}