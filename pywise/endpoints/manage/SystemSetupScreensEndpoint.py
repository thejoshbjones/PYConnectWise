from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemSetupScreensIdEndpoint import SystemSetupScreensIdEndpoint
from pywise.endpoints.manage.SystemSetupScreensCountEndpoint import SystemSetupScreensCountEndpoint
from pywise.models.manage.SetupScreenModel import SetupScreenModel

class SystemSetupScreensEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "setupScreens", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemSetupScreensCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemSetupScreensIdEndpoint:
        child = SystemSetupScreensIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SetupScreenModel]:
        """
        Performs a GET request against the /system/setupScreens endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SetupScreenModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SetupScreenModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SetupScreenModel]:
        """
        Performs a GET request against the /system/setupScreens endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SetupScreenModel]: The parsed response data.
        """
        return self._parse_many(SetupScreenModel, super().make_request("GET", params=params).json())
        