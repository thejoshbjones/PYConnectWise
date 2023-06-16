from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMembersIdPersonasIdEndpoint import SystemMembersIdPersonasIdEndpoint
from pywise.endpoints.SystemMembersIdPersonasCountEndpoint import SystemMembersIdPersonasCountEndpoint
from pywise.models.MemberPersonaModel import MemberPersonaModel

class SystemMembersIdPersonasEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "personas", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersIdPersonasCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMembersIdPersonasIdEndpoint:
        child = SystemMembersIdPersonasIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MemberPersonaModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MemberPersonaModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MemberPersonaModel]:
        return self._parse_many(MemberPersonaModel, super().make_request("GET", params=params))
        