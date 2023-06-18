from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemAllowedoriginsIdEndpoint import SystemAllowedoriginsIdEndpoint
from pywise.endpoints.manage.SystemAllowedoriginsCountEndpoint import SystemAllowedoriginsCountEndpoint
from pywise.models.manage.AllowedOriginModel import AllowedOriginModel

class SystemAllowedoriginsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "allowedorigins", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemAllowedoriginsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemAllowedoriginsIdEndpoint:
        child = SystemAllowedoriginsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AllowedOriginModel]:
        """
        Performs a GET request against the /system/allowedorigins endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AllowedOriginModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AllowedOriginModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AllowedOriginModel]:
        """
        Performs a GET request against the /system/allowedorigins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AllowedOriginModel]: The parsed response data.
        """
        return self._parse_many(AllowedOriginModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AllowedOriginModel:
        """
        Performs a POST request against the /system/allowedorigins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AllowedOriginModel: The parsed response data.
        """
        return self._parse_one(AllowedOriginModel, super().make_request("POST", params=params).json())
        