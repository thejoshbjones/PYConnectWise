from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyCompaniesIdEndpoint import CompanyCompaniesIdEndpoint
from pywise.endpoints.manage.CompanyCompaniesCountEndpoint import CompanyCompaniesCountEndpoint
from pywise.endpoints.manage.CompanyCompaniesDefaultEndpoint import CompanyCompaniesDefaultEndpoint
from pywise.endpoints.manage.CompanyCompaniesStatusesEndpoint import CompanyCompaniesStatusesEndpoint
from pywise.endpoints.manage.CompanyCompaniesTypesEndpoint import CompanyCompaniesTypesEndpoint
from pywise.models.manage.CompanyModel import CompanyModel

class CompanyCompaniesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "companies", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self.register_child_endpoint(
            CompanyCompaniesDefaultEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            CompanyCompaniesStatusesEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            CompanyCompaniesTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesIdEndpoint:
        child = CompanyCompaniesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyModel]:
        """
        Performs a GET request against the /company/companies endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanyModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyModel]:
        """
        Performs a GET request against the /company/companies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyModel]: The parsed response data.
        """
        return self._parse_many(CompanyModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyModel:
        """
        Performs a POST request against the /company/companies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyModel: The parsed response data.
        """
        return self._parse_one(CompanyModel, super().make_request("POST", params=params).json())
        