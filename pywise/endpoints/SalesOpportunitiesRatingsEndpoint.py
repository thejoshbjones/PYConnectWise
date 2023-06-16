from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesOpportunitiesRatingsIdEndpoint import SalesOpportunitiesRatingsIdEndpoint
from pywise.endpoints.SalesOpportunitiesRatingsCountEndpoint import SalesOpportunitiesRatingsCountEndpoint
from pywise.endpoints.SalesOpportunitiesRatingsInfoEndpoint import SalesOpportunitiesRatingsInfoEndpoint
from pywise.models.OpportunityRatingModel import OpportunityRatingModel

class SalesOpportunitiesRatingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ratings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesRatingsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SalesOpportunitiesRatingsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOpportunitiesRatingsIdEndpoint:
        child = SalesOpportunitiesRatingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OpportunityRatingModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OpportunityRatingModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OpportunityRatingModel]:
        return self._parse_many(OpportunityRatingModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> OpportunityRatingModel:
        return self._parse_one(OpportunityRatingModel, super().make_request("POST", params=params))
        