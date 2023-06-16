from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemSsoUsersIdEndpoint import SystemSsoUsersIdEndpoint
from pywise.endpoints.SystemSsoUsersCountEndpoint import SystemSsoUsersCountEndpoint
from pywise.models.SsoUserModel import SsoUserModel

class SystemSsoUsersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ssoUsers", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemSsoUsersCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemSsoUsersIdEndpoint:
        child = SystemSsoUsersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SsoUserModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SsoUserModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SsoUserModel]:
        return self._parse_many(SsoUserModel, super().make_request("GET", params=params))
        