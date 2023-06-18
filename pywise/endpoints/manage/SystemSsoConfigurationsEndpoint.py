from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemSsoConfigurationsIdEndpoint import SystemSsoConfigurationsIdEndpoint
from pywise.endpoints.manage.SystemSsoConfigurationsCountEndpoint import SystemSsoConfigurationsCountEndpoint
from pywise.models.manage.SsoConfigurationModel import SsoConfigurationModel

class SystemSsoConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ssoConfigurations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemSsoConfigurationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemSsoConfigurationsIdEndpoint:
        child = SystemSsoConfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SsoConfigurationModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SsoConfigurationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SsoConfigurationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SsoConfigurationModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SsoConfigurationModel]: The parsed response data.
        """
        return self._parse_many(SsoConfigurationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SsoConfigurationModel:
        """
        Performs a POST request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SsoConfigurationModel: The parsed response data.
        """
        return self._parse_one(SsoConfigurationModel, super().make_request("POST", params=params).json())
        