from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyManagementItSolutionsIdManagementProductsIdEndpoint import CompanyManagementItSolutionsIdManagementProductsIdEndpoint
from pywise.endpoints.manage.CompanyManagementItSolutionsIdManagementProductsCountEndpoint import CompanyManagementItSolutionsIdManagementProductsCountEndpoint
from pywise.models.manage.ManagementItSolutionAgreementInterfaceParameterModel import ManagementItSolutionAgreementInterfaceParameterModel

class CompanyManagementItSolutionsIdManagementProductsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementProducts", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagementItSolutionsIdManagementProductsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyManagementItSolutionsIdManagementProductsIdEndpoint:
        child = CompanyManagementItSolutionsIdManagementProductsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ManagementItSolutionAgreementInterfaceParameterModel]:
        """
        Performs a GET request against the /company/managementItSolutions/{parentId}/managementProducts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagementItSolutionAgreementInterfaceParameterModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ManagementItSolutionAgreementInterfaceParameterModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagementItSolutionAgreementInterfaceParameterModel]:
        """
        Performs a GET request against the /company/managementItSolutions/{parentId}/managementProducts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagementItSolutionAgreementInterfaceParameterModel]: The parsed response data.
        """
        return self._parse_many(ManagementItSolutionAgreementInterfaceParameterModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagementItSolutionAgreementInterfaceParameterModel:
        """
        Performs a POST request against the /company/managementItSolutions/{parentId}/managementProducts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementItSolutionAgreementInterfaceParameterModel: The parsed response data.
        """
        return self._parse_one(ManagementItSolutionAgreementInterfaceParameterModel, super().make_request("POST", params=params).json())
        