from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesSalesTeamsIdMembersIdEndpoint import SalesSalesTeamsIdMembersIdEndpoint
from pywise.endpoints.SalesSalesTeamsIdMembersCountEndpoint import SalesSalesTeamsIdMembersCountEndpoint
from pywise.models.SalesTeamMemberModel import SalesTeamMemberModel

class SalesSalesTeamsIdMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "members", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesSalesTeamsIdMembersCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesSalesTeamsIdMembersIdEndpoint:
        child = SalesSalesTeamsIdMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SalesTeamMemberModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SalesTeamMemberModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SalesTeamMemberModel]:
        return self._parse_many(SalesTeamMemberModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SalesTeamMemberModel:
        return self._parse_one(SalesTeamMemberModel, super().make_request("POST", params=params))
        