from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyCompaniesIdManagementReportSetupIdEndpoint import CompanyCompaniesIdManagementReportSetupIdEndpoint
from pywise.models.manage.ManagementReportSetupModel import ManagementReportSetupModel

class CompanyCompaniesIdManagementReportSetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementReportSetup", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> CompanyCompaniesIdManagementReportSetupIdEndpoint:
        child = CompanyCompaniesIdManagementReportSetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ManagementReportSetupModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/managementReportSetup endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagementReportSetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ManagementReportSetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagementReportSetupModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/managementReportSetup endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagementReportSetupModel]: The parsed response data.
        """
        return self._parse_many(ManagementReportSetupModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagementReportSetupModel:
        """
        Performs a POST request against the /company/companies/{parentId}/managementReportSetup endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementReportSetupModel: The parsed response data.
        """
        return self._parse_one(ManagementReportSetupModel, super().make_request("POST", params=params).json())
        