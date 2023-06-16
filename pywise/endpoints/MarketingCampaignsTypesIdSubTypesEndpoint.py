from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.MarketingCampaignsTypesIdSubTypesIdEndpoint import MarketingCampaignsTypesIdSubTypesIdEndpoint
from pywise.endpoints.MarketingCampaignsTypesIdSubTypesCountEndpoint import MarketingCampaignsTypesIdSubTypesCountEndpoint
from pywise.models.CampaignSubTypeModel import CampaignSubTypeModel

class MarketingCampaignsTypesIdSubTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "subTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsTypesIdSubTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> MarketingCampaignsTypesIdSubTypesIdEndpoint:
        child = MarketingCampaignsTypesIdSubTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CampaignSubTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CampaignSubTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CampaignSubTypeModel]:
        return self._parse_many(CampaignSubTypeModel, super().make_request("GET", params=params))
        