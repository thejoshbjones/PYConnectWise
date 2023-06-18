from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemCustomReportsIdParametersIdEndpoint import SystemCustomReportsIdParametersIdEndpoint
from pywise.endpoints.manage.SystemCustomReportsIdParametersCountEndpoint import SystemCustomReportsIdParametersCountEndpoint
from pywise.models.manage.CustomReportParameterModel import CustomReportParameterModel

class SystemCustomReportsIdParametersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parameters", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemCustomReportsIdParametersCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemCustomReportsIdParametersIdEndpoint:
        child = SystemCustomReportsIdParametersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CustomReportParameterModel]:
        """
        Performs a GET request against the /system/customReports/{parentId}/parameters endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CustomReportParameterModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CustomReportParameterModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CustomReportParameterModel]:
        """
        Performs a GET request against the /system/customReports/{parentId}/parameters endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CustomReportParameterModel]: The parsed response data.
        """
        return self._parse_many(CustomReportParameterModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CustomReportParameterModel:
        """
        Performs a POST request against the /system/customReports/{parentId}/parameters endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CustomReportParameterModel: The parsed response data.
        """
        return self._parse_one(CustomReportParameterModel, super().make_request("POST", params=params).json())
        