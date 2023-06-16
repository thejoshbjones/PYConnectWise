from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesOpportunitiesStatusesIdEndpoint import SalesOpportunitiesStatusesIdEndpoint
from pywise.endpoints.SalesOpportunitiesStatusesCountEndpoint import SalesOpportunitiesStatusesCountEndpoint
from pywise.endpoints.SalesOpportunitiesStatusesInfoEndpoint import SalesOpportunitiesStatusesInfoEndpoint
from pywise.models.OpportunityStatusModel import OpportunityStatusModel

class SalesOpportunitiesStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SalesOpportunitiesStatusesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOpportunitiesStatusesIdEndpoint:
        child = SalesOpportunitiesStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OpportunityStatusModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OpportunityStatusModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OpportunityStatusModel]:
        return self._parse_many(OpportunityStatusModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> OpportunityStatusModel:
        return self._parse_one(OpportunityStatusModel, super().make_request("POST", params=params))
        