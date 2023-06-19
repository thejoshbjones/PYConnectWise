from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemPortalReportsIdEndpoint import SystemPortalReportsIdEndpoint
from pywise.endpoints.manage.SystemPortalReportsCountEndpoint import SystemPortalReportsCountEndpoint
from pywise.models.manage.PortalReportModel import PortalReportModel

class SystemPortalReportsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "portalReports", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemPortalReportsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemPortalReportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemPortalReportsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemPortalReportsIdEndpoint: The initialized SystemPortalReportsIdEndpoint object.
        """
        child = SystemPortalReportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PortalReportModel]:
        """
        Performs a GET request against the /system/portalReports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalReportModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PortalReportModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PortalReportModel]:
        """
        Performs a GET request against the /system/portalReports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalReportModel]: The parsed response data.
        """
        return self._parse_many(PortalReportModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalReportModel:
        """
        Performs a POST request against the /system/portalReports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalReportModel: The parsed response data.
        """
        return self._parse_one(PortalReportModel, super().make_request("POST", params=params).json())
        