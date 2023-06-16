from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.MarketingCampaignsIdAuditsIdEndpoint import MarketingCampaignsIdAuditsIdEndpoint
from pywise.endpoints.MarketingCampaignsIdAuditsCountEndpoint import MarketingCampaignsIdAuditsCountEndpoint
from pywise.models.CampaignAuditModel import CampaignAuditModel

class MarketingCampaignsIdAuditsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "audits", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsIdAuditsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> MarketingCampaignsIdAuditsIdEndpoint:
        child = MarketingCampaignsIdAuditsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CampaignAuditModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CampaignAuditModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CampaignAuditModel]:
        return self._parse_many(CampaignAuditModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CampaignAuditModel:
        return self._parse_one(CampaignAuditModel, super().make_request("POST", params=params))
        