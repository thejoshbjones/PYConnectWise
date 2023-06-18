from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemInfoLocalesIdEndpoint import SystemInfoLocalesIdEndpoint
from pywise.endpoints.manage.SystemInfoLocalesCountEndpoint import SystemInfoLocalesCountEndpoint
from pywise.models.manage.LocaleInfoModel import LocaleInfoModel

class SystemInfoLocalesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locales", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoLocalesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemInfoLocalesIdEndpoint:
        child = SystemInfoLocalesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[LocaleInfoModel]:
        """
        Performs a GET request against the /system/info/locales endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LocaleInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            LocaleInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LocaleInfoModel]:
        """
        Performs a GET request against the /system/info/locales endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LocaleInfoModel]: The parsed response data.
        """
        return self._parse_many(LocaleInfoModel, super().make_request("GET", params=params).json())
        