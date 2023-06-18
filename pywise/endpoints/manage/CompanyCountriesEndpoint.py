from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyCountriesIdEndpoint import CompanyCountriesIdEndpoint
from pywise.endpoints.manage.CompanyCountriesCountEndpoint import CompanyCountriesCountEndpoint
from pywise.endpoints.manage.CompanyCountriesInfoEndpoint import CompanyCountriesInfoEndpoint
from pywise.models.manage.CountryModel import CountryModel

class CompanyCountriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "countries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCountriesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyCountriesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCountriesIdEndpoint:
        child = CompanyCountriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CountryModel]:
        """
        Performs a GET request against the /company/countries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CountryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CountryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CountryModel]:
        """
        Performs a GET request against the /company/countries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CountryModel]: The parsed response data.
        """
        return self._parse_many(CountryModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CountryModel:
        """
        Performs a POST request against the /company/countries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CountryModel: The parsed response data.
        """
        return self._parse_one(CountryModel, super().make_request("POST", params=params).json())
        