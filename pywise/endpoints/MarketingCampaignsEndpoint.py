from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.MarketingCampaignsIdEndpoint import MarketingCampaignsIdEndpoint
from pywise.endpoints.MarketingCampaignsCountEndpoint import MarketingCampaignsCountEndpoint
from pywise.endpoints.MarketingCampaignsStatusesEndpoint import MarketingCampaignsStatusesEndpoint
from pywise.endpoints.MarketingCampaignsSubTypesEndpoint import MarketingCampaignsSubTypesEndpoint
from pywise.endpoints.MarketingCampaignsTypesEndpoint import MarketingCampaignsTypesEndpoint
from pywise.models.CampaignModel import CampaignModel

class MarketingCampaignsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "campaigns", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsCountEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            MarketingCampaignsStatusesEndpoint(client, parent_endpoint=self)
        )
        self.subTypes = self.register_child_endpoint(
            MarketingCampaignsSubTypesEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            MarketingCampaignsTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> MarketingCampaignsIdEndpoint:
        child = MarketingCampaignsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CampaignModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CampaignModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CampaignModel]:
        return self._parse_many(CampaignModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CampaignModel:
        return self._parse_one(CampaignModel, super().make_request("POST", params=params))
        