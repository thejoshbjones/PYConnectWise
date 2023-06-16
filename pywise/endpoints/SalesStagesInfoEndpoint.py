from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesStagesInfoCountEndpoint import SalesStagesInfoCountEndpoint
from pywise.models.OpportunityStageInfoModel import OpportunityStageInfoModel

class SalesStagesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesStagesInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OpportunityStageInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OpportunityStageInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OpportunityStageInfoModel]:
        return self._parse_many(OpportunityStageInfoModel, super().make_request("GET", params=params))
        