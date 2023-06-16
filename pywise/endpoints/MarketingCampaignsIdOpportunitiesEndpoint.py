from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.MarketingCampaignsIdOpportunitiesCountEndpoint import MarketingCampaignsIdOpportunitiesCountEndpoint
from pywise.models.OpportunityReferenceModel import OpportunityReferenceModel

class MarketingCampaignsIdOpportunitiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "opportunities", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsIdOpportunitiesCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OpportunityReferenceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OpportunityReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OpportunityReferenceModel]:
        return self._parse_many(OpportunityReferenceModel, super().make_request("GET", params=params))
        