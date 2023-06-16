from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemLdapConfigurationsIdEndpoint import SystemLdapConfigurationsIdEndpoint
from pywise.endpoints.SystemLdapConfigurationsCountEndpoint import SystemLdapConfigurationsCountEndpoint
from pywise.endpoints.SystemLdapConfigurationsInfoEndpoint import SystemLdapConfigurationsInfoEndpoint
from pywise.endpoints.SystemLdapConfigurationsTestLinkEndpoint import SystemLdapConfigurationsTestLinkEndpoint
from pywise.models.LdapConfigurationModel import LdapConfigurationModel

class SystemLdapConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ldapConfigurations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemLdapConfigurationsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemLdapConfigurationsInfoEndpoint(client, parent_endpoint=self)
        )
        self.testLink = self.register_child_endpoint(
            SystemLdapConfigurationsTestLinkEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemLdapConfigurationsIdEndpoint:
        child = SystemLdapConfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[LdapConfigurationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            LdapConfigurationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[LdapConfigurationModel]:
        return self._parse_many(LdapConfigurationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> LdapConfigurationModel:
        return self._parse_one(LdapConfigurationModel, super().make_request("POST", params=params))
        