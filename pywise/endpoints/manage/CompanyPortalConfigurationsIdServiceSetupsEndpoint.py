from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyPortalConfigurationsIdServiceSetupsIdEndpoint import CompanyPortalConfigurationsIdServiceSetupsIdEndpoint
from pywise.endpoints.manage.CompanyPortalConfigurationsIdServiceSetupsCountEndpoint import CompanyPortalConfigurationsIdServiceSetupsCountEndpoint
from pywise.models.manage.PortalConfigurationServiceSetupModel import PortalConfigurationServiceSetupModel

class CompanyPortalConfigurationsIdServiceSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "serviceSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyPortalConfigurationsIdServiceSetupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyPortalConfigurationsIdServiceSetupsIdEndpoint:
        child = CompanyPortalConfigurationsIdServiceSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PortalConfigurationServiceSetupModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationServiceSetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PortalConfigurationServiceSetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PortalConfigurationServiceSetupModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfigurationServiceSetupModel]: The parsed response data.
        """
        return self._parse_many(PortalConfigurationServiceSetupModel, super().make_request("GET", params=params).json())
        