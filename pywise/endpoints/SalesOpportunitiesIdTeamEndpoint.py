from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesOpportunitiesIdTeamIdEndpoint import SalesOpportunitiesIdTeamIdEndpoint
from pywise.endpoints.SalesOpportunitiesIdTeamCountEndpoint import SalesOpportunitiesIdTeamCountEndpoint
from pywise.models.TeamModel import TeamModel

class SalesOpportunitiesIdTeamEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "team", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesIdTeamCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOpportunitiesIdTeamIdEndpoint:
        child = SalesOpportunitiesIdTeamIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TeamModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TeamModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TeamModel]:
        return self._parse_many(TeamModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TeamModel:
        return self._parse_one(TeamModel, super().make_request("POST", params=params))
        