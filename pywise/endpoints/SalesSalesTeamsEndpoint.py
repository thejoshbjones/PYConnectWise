from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesSalesTeamsIdEndpoint import SalesSalesTeamsIdEndpoint
from pywise.endpoints.SalesSalesTeamsCountEndpoint import SalesSalesTeamsCountEndpoint
from pywise.models.SalesTeamModel import SalesTeamModel

class SalesSalesTeamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "salesTeams", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesSalesTeamsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesSalesTeamsIdEndpoint:
        child = SalesSalesTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SalesTeamModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SalesTeamModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SalesTeamModel]:
        return self._parse_many(SalesTeamModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SalesTeamModel:
        return self._parse_one(SalesTeamModel, super().make_request("POST", params=params))
        