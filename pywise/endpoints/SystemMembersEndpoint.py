from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMembersIdEndpoint import SystemMembersIdEndpoint
from pywise.endpoints.SystemMembersIdEndpoint import SystemMembersIdEndpoint
from pywise.endpoints.SystemMembersCountEndpoint import SystemMembersCountEndpoint
from pywise.endpoints.SystemMembersTypesEndpoint import SystemMembersTypesEndpoint
from pywise.endpoints.SystemMembersWithSsoEndpoint import SystemMembersWithSsoEndpoint
from pywise.models.MemberModel import MemberModel

class SystemMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "members", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersCountEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            SystemMembersTypesEndpoint(client, parent_endpoint=self)
        )
        self.withSso = self.register_child_endpoint(
            SystemMembersWithSsoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMembersIdEndpoint:
        child = SystemMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MemberModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MemberModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MemberModel]:
        return self._parse_many(MemberModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MemberModel:
        return self._parse_one(MemberModel, super().make_request("POST", params=params))
        