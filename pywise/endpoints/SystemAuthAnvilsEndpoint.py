from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemAuthAnvilsIdEndpoint import SystemAuthAnvilsIdEndpoint
from pywise.endpoints.SystemAuthAnvilsCountEndpoint import SystemAuthAnvilsCountEndpoint
from pywise.endpoints.SystemAuthAnvilsTestConnectionEndpoint import SystemAuthAnvilsTestConnectionEndpoint
from pywise.models.AuthAnvilModel import AuthAnvilModel

class SystemAuthAnvilsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "authAnvils", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemAuthAnvilsCountEndpoint(client, parent_endpoint=self)
        )
        self.testConnection = self.register_child_endpoint(
            SystemAuthAnvilsTestConnectionEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemAuthAnvilsIdEndpoint:
        child = SystemAuthAnvilsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AuthAnvilModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AuthAnvilModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AuthAnvilModel]:
        return self._parse_many(AuthAnvilModel, super().make_request("GET", params=params))
        