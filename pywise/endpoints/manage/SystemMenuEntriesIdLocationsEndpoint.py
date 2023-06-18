from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemMenuEntriesIdLocationsIdEndpoint import SystemMenuEntriesIdLocationsIdEndpoint
from pywise.endpoints.manage.SystemMenuEntriesIdLocationsCountEndpoint import SystemMenuEntriesIdLocationsCountEndpoint
from pywise.models.manage.MenuEntryLocationModel import MenuEntryLocationModel

class SystemMenuEntriesIdLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMenuEntriesIdLocationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMenuEntriesIdLocationsIdEndpoint:
        child = SystemMenuEntriesIdLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MenuEntryLocationModel]:
        """
        Performs a GET request against the /system/menuEntries/{parentId}/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MenuEntryLocationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MenuEntryLocationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MenuEntryLocationModel]:
        """
        Performs a GET request against the /system/menuEntries/{parentId}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MenuEntryLocationModel]: The parsed response data.
        """
        return self._parse_many(MenuEntryLocationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MenuEntryLocationModel:
        """
        Performs a POST request against the /system/menuEntries/{parentId}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MenuEntryLocationModel: The parsed response data.
        """
        return self._parse_one(MenuEntryLocationModel, super().make_request("POST", params=params).json())
        