from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesOpportunitiesIdEndpoint import SalesOpportunitiesIdEndpoint
from pywise.endpoints.SalesOpportunitiesCountEndpoint import SalesOpportunitiesCountEndpoint
from pywise.endpoints.SalesOpportunitiesDefaultEndpoint import SalesOpportunitiesDefaultEndpoint
from pywise.endpoints.SalesOpportunitiesRatingsEndpoint import SalesOpportunitiesRatingsEndpoint
from pywise.endpoints.SalesOpportunitiesStatusesEndpoint import SalesOpportunitiesStatusesEndpoint
from pywise.endpoints.SalesOpportunitiesTypesEndpoint import SalesOpportunitiesTypesEndpoint
from pywise.models.OpportunityModel import OpportunityModel

class SalesOpportunitiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "opportunities", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self.register_child_endpoint(
            SalesOpportunitiesDefaultEndpoint(client, parent_endpoint=self)
        )
        self.ratings = self.register_child_endpoint(
            SalesOpportunitiesRatingsEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            SalesOpportunitiesStatusesEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            SalesOpportunitiesTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOpportunitiesIdEndpoint:
        child = SalesOpportunitiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OpportunityModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OpportunityModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OpportunityModel]:
        return self._parse_many(OpportunityModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> OpportunityModel:
        return self._parse_one(OpportunityModel, super().make_request("POST", params=params))
        