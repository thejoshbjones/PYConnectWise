from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.MarketingCampaignsTypesIdEndpoint import MarketingCampaignsTypesIdEndpoint
from pywise.endpoints.MarketingCampaignsTypesCountEndpoint import MarketingCampaignsTypesCountEndpoint
from pywise.endpoints.MarketingCampaignsTypesInfoEndpoint import MarketingCampaignsTypesInfoEndpoint
from pywise.models.CampaignTypeModel import CampaignTypeModel

class MarketingCampaignsTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            MarketingCampaignsTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> MarketingCampaignsTypesIdEndpoint:
        child = MarketingCampaignsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CampaignTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CampaignTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CampaignTypeModel]:
        return self._parse_many(CampaignTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CampaignTypeModel:
        return self._parse_one(CampaignTypeModel, super().make_request("POST", params=params))
        