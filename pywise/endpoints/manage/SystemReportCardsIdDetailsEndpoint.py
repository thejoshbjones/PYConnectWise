from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemReportCardsIdDetailsIdEndpoint import SystemReportCardsIdDetailsIdEndpoint
from pywise.endpoints.manage.SystemReportCardsIdDetailsCountEndpoint import SystemReportCardsIdDetailsCountEndpoint
from pywise.models.manage.ReportCardDetailModel import ReportCardDetailModel

class SystemReportCardsIdDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "details", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemReportCardsIdDetailsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemReportCardsIdDetailsIdEndpoint:
        child = SystemReportCardsIdDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ReportCardDetailModel]:
        """
        Performs a GET request against the /system/reportCards/{parentId}/details endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ReportCardDetailModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ReportCardDetailModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ReportCardDetailModel]:
        """
        Performs a GET request against the /system/reportCards/{parentId}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ReportCardDetailModel]: The parsed response data.
        """
        return self._parse_many(ReportCardDetailModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ReportCardDetailModel:
        """
        Performs a POST request against the /system/reportCards/{parentId}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ReportCardDetailModel: The parsed response data.
        """
        return self._parse_one(ReportCardDetailModel, super().make_request("POST", params=params).json())
        