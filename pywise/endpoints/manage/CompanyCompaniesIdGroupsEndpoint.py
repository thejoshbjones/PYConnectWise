from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyCompaniesIdGroupsIdEndpoint import CompanyCompaniesIdGroupsIdEndpoint
from pywise.endpoints.manage.CompanyCompaniesIdGroupsCountEndpoint import CompanyCompaniesIdGroupsCountEndpoint
from pywise.models.manage.CompanyGroupModel import CompanyGroupModel

class CompanyCompaniesIdGroupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "groups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdGroupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesIdGroupsIdEndpoint:
        child = CompanyCompaniesIdGroupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyGroupModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/groups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyGroupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanyGroupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyGroupModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyGroupModel]: The parsed response data.
        """
        return self._parse_many(CompanyGroupModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyGroupModel:
        """
        Performs a POST request against the /company/companies/{parentId}/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyGroupModel: The parsed response data.
        """
        return self._parse_one(CompanyGroupModel, super().make_request("POST", params=params).json())
        