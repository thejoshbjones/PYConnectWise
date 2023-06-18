from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServiceSLAsIdPrioritiesIdEndpoint import ServiceSLAsIdPrioritiesIdEndpoint
from pywise.endpoints.manage.ServiceSLAsIdPrioritiesCountEndpoint import ServiceSLAsIdPrioritiesCountEndpoint
from pywise.models.manage.SLAPriorityModel import SLAPriorityModel

class ServiceSLAsIdPrioritiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "priorities", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceSLAsIdPrioritiesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceSLAsIdPrioritiesIdEndpoint:
        child = ServiceSLAsIdPrioritiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SLAPriorityModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SLAPriorityModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SLAPriorityModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SLAPriorityModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SLAPriorityModel]: The parsed response data.
        """
        return self._parse_many(SLAPriorityModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SLAPriorityModel:
        """
        Performs a POST request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SLAPriorityModel: The parsed response data.
        """
        return self._parse_one(SLAPriorityModel, super().make_request("POST", params=params).json())
        