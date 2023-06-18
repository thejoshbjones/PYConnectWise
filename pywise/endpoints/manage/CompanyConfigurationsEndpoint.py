from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyConfigurationsIdEndpoint import CompanyConfigurationsIdEndpoint
from pywise.endpoints.manage.CompanyConfigurationsBulkEndpoint import CompanyConfigurationsBulkEndpoint
from pywise.endpoints.manage.CompanyConfigurationsCountEndpoint import CompanyConfigurationsCountEndpoint
from pywise.endpoints.manage.CompanyConfigurationsStatusesEndpoint import CompanyConfigurationsStatusesEndpoint
from pywise.endpoints.manage.CompanyConfigurationsTypesEndpoint import CompanyConfigurationsTypesEndpoint
from pywise.models.manage.ConfigurationModel import ConfigurationModel

class CompanyConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "configurations", parent_endpoint=parent_endpoint)
        
        self.bulk = self.register_child_endpoint(
            CompanyConfigurationsBulkEndpoint(client, parent_endpoint=self)
        )
        self.count = self.register_child_endpoint(
            CompanyConfigurationsCountEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            CompanyConfigurationsStatusesEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            CompanyConfigurationsTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyConfigurationsIdEndpoint:
        child = CompanyConfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ConfigurationModel]:
        """
        Performs a GET request against the /company/configurations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ConfigurationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ConfigurationModel]:
        """
        Performs a GET request against the /company/configurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationModel]: The parsed response data.
        """
        return self._parse_many(ConfigurationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ConfigurationModel:
        """
        Performs a POST request against the /company/configurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationModel: The parsed response data.
        """
        return self._parse_one(ConfigurationModel, super().make_request("POST", params=params).json())
        