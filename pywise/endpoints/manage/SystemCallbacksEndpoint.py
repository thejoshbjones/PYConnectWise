from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemCallbacksIdEndpoint import SystemCallbacksIdEndpoint
from pywise.endpoints.manage.SystemCallbacksCountEndpoint import SystemCallbacksCountEndpoint
from pywise.models.manage.CallbackEntryModel import CallbackEntryModel

class SystemCallbacksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "callbacks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemCallbacksCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemCallbacksIdEndpoint:
        child = SystemCallbacksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CallbackEntryModel]:
        """
        Performs a GET request against the /system/callbacks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CallbackEntryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CallbackEntryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CallbackEntryModel]:
        """
        Performs a GET request against the /system/callbacks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CallbackEntryModel]: The parsed response data.
        """
        return self._parse_many(CallbackEntryModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CallbackEntryModel:
        """
        Performs a POST request against the /system/callbacks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CallbackEntryModel: The parsed response data.
        """
        return self._parse_one(CallbackEntryModel, super().make_request("POST", params=params).json())
        