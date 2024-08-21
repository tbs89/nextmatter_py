class NextMatterException(Exception):
    """
    A ``NextMatterException`` is raised for internal errors.
    """


class NextMatterCacheException(NextMatterException):
    """
    A ``NextMatterCacheException`` is raised for errors relating to the cache.
    """


class RatelimitBudgetExceeded(NextMatterException):
    """
    A ``RatelimitBudgetExceeded`` is raised when the ratelimit budget has been spent.
    """


class APIException(Exception):
    """
    An ``APIException`` is raised when the API rejects a query.
    """
    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        super(APIException, self).__init__(*args)


class RecordNotFoundException(APIException):
    """
    A ``RecordNotFoundException`` is raised when the API cannot find a record.
    """


class TooManyValuesException(APIException):
    """
    A ``TooManyValuesException`` is raised when too many values
    have been passed to an endpoint.
    """


class SearchResponseLimitExceeded(APIException):
    """
    A ``SearchResponseLimitExceeded`` is raised when a search has too many results.
    """


class InvalidQueryParamException(APIException):
    """
    An ``InvalidQueryParamException`` is raised when an invalid query parameter is passed.
    """
    def __init__(self, invalid_param: str, valid_params: list, *args, **kwargs):
        self.invalid_param = invalid_param
        self.valid_params = valid_params
        message = f"Invalid query parameter: '{invalid_param}'. Valid query parameters are: {', '.join(valid_params)}"
        super().__init__(message, *args, **kwargs)


class InvalidBodyParamException(APIException):
    """
    An ``InvalidBodyParamException`` is raised when an invalid body parameter is passed.
    """
    def __init__(self, invalid_param: str, valid_params: list, *args, **kwargs):
        self.invalid_param = invalid_param
        self.valid_params = valid_params
        message = f"Invalid body parameter: '{invalid_param}'. Valid body parameters are: {', '.join(valid_params)}"
        super().__init__(message, *args, **kwargs)


class InvalidPathParamException(APIException):
    """
    An ``InvalidPathParamException`` is raised when an invalid path parameter is passed.
    """
    def __init__(self, invalid_param: str, valid_params: list, *args, **kwargs):
        self.invalid_param = invalid_param
        self.valid_params = valid_params
        message = f"Invalid path parameter: '{invalid_param}'. Valid path parameters are: {', '.join(valid_params)}"
        super().__init__(message, *args, **kwargs)

class InvalidPageSizeException(APIException):
    """
    An ``InvalidPageSizeException`` is raised when the page size exceeds the allowed limit.
    """
    def __init__(self, page_size: int, max_page_size: int = 500, *args, **kwargs):
        self.page_size = page_size
        self.max_page_size = max_page_size
        message = f"Invalid page size: {page_size}. Page size cannot exceed {max_page_size}."
        super().__init__(message, *args, **kwargs)