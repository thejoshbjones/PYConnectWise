from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMembersTypesInfoCountEndpoint import SystemMembersTypesInfoCountEndpoint
from pywise.models.MemberTypeInfoModel import MemberTypeInfoModel

class SystemMembersTypesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersTypesInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MemberTypeInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MemberTypeInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MemberTypeInfoModel]:
        return self._parse_many(MemberTypeInfoModel, super().make_request("GET", params=params))
        