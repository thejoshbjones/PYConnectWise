from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesStagesIdEndpoint import SalesStagesIdEndpoint
from pywise.endpoints.SalesStagesCountEndpoint import SalesStagesCountEndpoint
from pywise.endpoints.SalesStagesInfoEndpoint import SalesStagesInfoEndpoint
from pywise.models.OpportunityStageModel import OpportunityStageModel

class SalesStagesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "stages", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesStagesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SalesStagesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesStagesIdEndpoint:
        child = SalesStagesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OpportunityStageModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OpportunityStageModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OpportunityStageModel]:
        return self._parse_many(OpportunityStageModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> OpportunityStageModel:
        return self._parse_one(OpportunityStageModel, super().make_request("POST", params=params))
        