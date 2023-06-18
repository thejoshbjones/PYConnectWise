from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemCwTimeZonesIdEndpoint import SystemCwTimeZonesIdEndpoint
from pywise.endpoints.manage.SystemCwTimeZonesCountEndpoint import SystemCwTimeZonesCountEndpoint
from pywise.models.manage.CwTimeZoneModel import CwTimeZoneModel

class SystemCwTimeZonesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "cwTimeZones", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemCwTimeZonesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemCwTimeZonesIdEndpoint:
        child = SystemCwTimeZonesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CwTimeZoneModel]:
        """
        Performs a GET request against the /system/cwTimeZones endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CwTimeZoneModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CwTimeZoneModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CwTimeZoneModel]:
        """
        Performs a GET request against the /system/cwTimeZones endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CwTimeZoneModel]: The parsed response data.
        """
        return self._parse_many(CwTimeZoneModel, super().make_request("GET", params=params).json())
        