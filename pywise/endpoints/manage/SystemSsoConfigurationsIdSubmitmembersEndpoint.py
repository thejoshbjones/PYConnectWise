from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.models.manage.SsoConfigurationModel import SsoConfigurationModel

class SystemSsoConfigurationsIdSubmitmembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "submitmembers", parent_endpoint=parent_endpoint)
        
    
    
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SsoConfigurationModel:
        """
        Performs a POST request against the /system/ssoConfigurations/{id}/submitmembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SsoConfigurationModel: The parsed response data.
        """
        return self._parse_one(SsoConfigurationModel, super().make_request("POST", params=params).json())
        