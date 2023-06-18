from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemMenuentriesIdEndpoint import SystemMenuentriesIdEndpoint
from pywise.endpoints.manage.SystemMenuentriesCountEndpoint import SystemMenuentriesCountEndpoint
from pywise.models.manage.MenuEntryModel import MenuEntryModel

class SystemMenuentriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "menuentries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMenuentriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMenuentriesIdEndpoint:
        child = SystemMenuentriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MenuEntryModel]:
        """
        Performs a GET request against the /system/menuentries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MenuEntryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MenuEntryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MenuEntryModel]:
        """
        Performs a GET request against the /system/menuentries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MenuEntryModel]: The parsed response data.
        """
        return self._parse_many(MenuEntryModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MenuEntryModel:
        """
        Performs a POST request against the /system/menuentries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MenuEntryModel: The parsed response data.
        """
        return self._parse_one(MenuEntryModel, super().make_request("POST", params=params).json())
        