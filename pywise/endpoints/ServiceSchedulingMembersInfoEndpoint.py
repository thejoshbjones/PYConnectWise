from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceSchedulingMembersInfoCountEndpoint import ServiceSchedulingMembersInfoCountEndpoint
from pywise.models.SchedulingMemberInfoModel import SchedulingMemberInfoModel

class ServiceSchedulingMembersInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceSchedulingMembersInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SchedulingMemberInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SchedulingMemberInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SchedulingMemberInfoModel]:
        return self._parse_many(SchedulingMemberInfoModel, super().make_request("GET", params=params))
        