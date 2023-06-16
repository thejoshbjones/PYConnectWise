from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemInfoMembersIdEndpoint import SystemInfoMembersIdEndpoint
from pywise.endpoints.SystemInfoMembersIdEndpoint import SystemInfoMembersIdEndpoint
from pywise.endpoints.SystemInfoMembersCountEndpoint import SystemInfoMembersCountEndpoint
from pywise.models.MemberInfoModel import MemberInfoModel

class SystemInfoMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "members", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoMembersCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemInfoMembersIdEndpoint:
        child = SystemInfoMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MemberInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MemberInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MemberInfoModel]:
        return self._parse_many(MemberInfoModel, super().make_request("GET", params=params))
        