from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMembersIdSkillsIdEndpoint import SystemMembersIdSkillsIdEndpoint
from pywise.endpoints.SystemMembersIdSkillsCountEndpoint import SystemMembersIdSkillsCountEndpoint
from pywise.models.MemberSkillModel import MemberSkillModel

class SystemMembersIdSkillsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "skills", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersIdSkillsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMembersIdSkillsIdEndpoint:
        child = SystemMembersIdSkillsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MemberSkillModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MemberSkillModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MemberSkillModel]:
        return self._parse_many(MemberSkillModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MemberSkillModel:
        return self._parse_one(MemberSkillModel, super().make_request("POST", params=params))
        