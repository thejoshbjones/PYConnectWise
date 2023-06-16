from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemSecurityrolesIdEndpoint import SystemSecurityrolesIdEndpoint
from pywise.endpoints.SystemSecurityrolesCountEndpoint import SystemSecurityrolesCountEndpoint
from pywise.endpoints.SystemSecurityrolesInfoEndpoint import SystemSecurityrolesInfoEndpoint
from pywise.models.SecurityRoleModel import SecurityRoleModel

class SystemSecurityrolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "securityroles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemSecurityrolesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemSecurityrolesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemSecurityrolesIdEndpoint:
        child = SystemSecurityrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SecurityRoleModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SecurityRoleModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SecurityRoleModel]:
        return self._parse_many(SecurityRoleModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SecurityRoleModel:
        return self._parse_one(SecurityRoleModel, super().make_request("POST", params=params))
        