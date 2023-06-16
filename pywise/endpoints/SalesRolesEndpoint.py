from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesRolesIdEndpoint import SalesRolesIdEndpoint
from pywise.endpoints.SalesRolesCountEndpoint import SalesRolesCountEndpoint
from pywise.models.RoleModel import RoleModel

class SalesRolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "roles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesRolesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesRolesIdEndpoint:
        child = SalesRolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[RoleModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            RoleModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[RoleModel]:
        return self._parse_many(RoleModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> RoleModel:
        return self._parse_one(RoleModel, super().make_request("POST", params=params))
        