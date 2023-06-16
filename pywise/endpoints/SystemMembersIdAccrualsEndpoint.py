from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMembersIdAccrualsIdEndpoint import SystemMembersIdAccrualsIdEndpoint
from pywise.endpoints.SystemMembersIdAccrualsCountEndpoint import SystemMembersIdAccrualsCountEndpoint
from pywise.models.MemberAccrualModel import MemberAccrualModel

class SystemMembersIdAccrualsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "accruals", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersIdAccrualsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMembersIdAccrualsIdEndpoint:
        child = SystemMembersIdAccrualsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MemberAccrualModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MemberAccrualModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MemberAccrualModel]:
        return self._parse_many(MemberAccrualModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MemberAccrualModel:
        return self._parse_one(MemberAccrualModel, super().make_request("POST", params=params))
        