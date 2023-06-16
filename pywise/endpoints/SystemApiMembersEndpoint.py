from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemApiMembersIdEndpoint import SystemApiMembersIdEndpoint
from pywise.endpoints.SystemApiMembersCountEndpoint import SystemApiMembersCountEndpoint
from pywise.endpoints.SystemApiMembersDefaultEndpoint import SystemApiMembersDefaultEndpoint
from pywise.models.ApiMemberModel import ApiMemberModel

class SystemApiMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "apiMembers", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemApiMembersCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self.register_child_endpoint(
            SystemApiMembersDefaultEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemApiMembersIdEndpoint:
        child = SystemApiMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ApiMemberModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ApiMemberModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ApiMemberModel]:
        return self._parse_many(ApiMemberModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ApiMemberModel:
        return self._parse_one(ApiMemberModel, super().make_request("POST", params=params))
        