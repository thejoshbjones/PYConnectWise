from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMembersTypesIdEndpoint import SystemMembersTypesIdEndpoint
from pywise.endpoints.SystemMembersTypesCountEndpoint import SystemMembersTypesCountEndpoint
from pywise.endpoints.SystemMembersTypesInfoEndpoint import SystemMembersTypesInfoEndpoint
from pywise.models.MemberTypeModel import MemberTypeModel

class SystemMembersTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemMembersTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMembersTypesIdEndpoint:
        child = SystemMembersTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MemberTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MemberTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MemberTypeModel]:
        return self._parse_many(MemberTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MemberTypeModel:
        return self._parse_one(MemberTypeModel, super().make_request("POST", params=params))
        