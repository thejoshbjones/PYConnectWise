from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.models.manage.ConfigurationModel import ConfigurationModel

class CompanyConfigurationsIdChangeTypeEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "changeType", parent_endpoint=parent_endpoint)
        
    
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ConfigurationModel:
        """
        Performs a PATCH request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationModel: The parsed response data.
        """
        return self._parse_one(ConfigurationModel, super().make_request("PATCH", params=params).json())
        