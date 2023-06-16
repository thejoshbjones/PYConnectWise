from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMyMembersInfoEndpoint import SystemMyMembersInfoEndpoint
from pywise.models.MyMemberModel import MyMemberModel

class SystemMyMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "myMembers", parent_endpoint=parent_endpoint)
        
        self.info = self.register_child_endpoint(
            SystemMyMembersInfoEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MyMemberModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MyMemberModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> MyMemberModel:
        return self._parse_one(MyMemberModel, super().make_request("GET", params=params))
        