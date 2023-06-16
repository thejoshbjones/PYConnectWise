from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.MarketingCampaignsStatusesIdEndpoint import MarketingCampaignsStatusesIdEndpoint
from pywise.endpoints.MarketingCampaignsStatusesCountEndpoint import MarketingCampaignsStatusesCountEndpoint
from pywise.models.CampaignStatusModel import CampaignStatusModel

class MarketingCampaignsStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsStatusesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> MarketingCampaignsStatusesIdEndpoint:
        child = MarketingCampaignsStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CampaignStatusModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CampaignStatusModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CampaignStatusModel]:
        return self._parse_many(CampaignStatusModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CampaignStatusModel:
        return self._parse_one(CampaignStatusModel, super().make_request("POST", params=params))
        