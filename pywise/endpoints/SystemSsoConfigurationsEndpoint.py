from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemSsoConfigurationsIdEndpoint import SystemSsoConfigurationsIdEndpoint
from pywise.endpoints.SystemSsoConfigurationsCountEndpoint import SystemSsoConfigurationsCountEndpoint
from pywise.models.SsoConfigurationModel import SsoConfigurationModel

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
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SsoConfigurationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SsoConfigurationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SsoConfigurationModel]:
        return self._parse_many(SsoConfigurationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SsoConfigurationModel:
        return self._parse_one(SsoConfigurationModel, super().make_request("POST", params=params))
        