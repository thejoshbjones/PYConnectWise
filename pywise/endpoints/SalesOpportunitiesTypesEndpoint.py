from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesOpportunitiesTypesIdEndpoint import SalesOpportunitiesTypesIdEndpoint
from pywise.endpoints.SalesOpportunitiesTypesCountEndpoint import SalesOpportunitiesTypesCountEndpoint
from pywise.endpoints.SalesOpportunitiesTypesInfoEndpoint import SalesOpportunitiesTypesInfoEndpoint
from pywise.models.OpportunityTypeModel import OpportunityTypeModel

class SalesOpportunitiesTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SalesOpportunitiesTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOpportunitiesTypesIdEndpoint:
        child = SalesOpportunitiesTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OpportunityTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OpportunityTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OpportunityTypeModel]:
        return self._parse_many(OpportunityTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> OpportunityTypeModel:
        return self._parse_one(OpportunityTypeModel, super().make_request("POST", params=params))
        