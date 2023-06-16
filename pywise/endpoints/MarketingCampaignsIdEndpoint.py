from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.MarketingCampaignsIdActivitiesEndpoint import MarketingCampaignsIdActivitiesEndpoint
from pywise.endpoints.MarketingCampaignsIdOpportunitiesEndpoint import MarketingCampaignsIdOpportunitiesEndpoint
from pywise.endpoints.MarketingCampaignsIdAuditsEndpoint import MarketingCampaignsIdAuditsEndpoint
from pywise.endpoints.MarketingCampaignsIdEmailsOpenedEndpoint import MarketingCampaignsIdEmailsOpenedEndpoint
from pywise.endpoints.MarketingCampaignsIdFormsSubmittedEndpoint import MarketingCampaignsIdFormsSubmittedEndpoint
from pywise.endpoints.MarketingCampaignsIdLinksClickedEndpoint import MarketingCampaignsIdLinksClickedEndpoint
from pywise.models.CampaignModel import CampaignModel

class MarketingCampaignsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.activities = self.register_child_endpoint(
            MarketingCampaignsIdActivitiesEndpoint(client, parent_endpoint=self)
        )
        self.opportunities = self.register_child_endpoint(
            MarketingCampaignsIdOpportunitiesEndpoint(client, parent_endpoint=self)
        )
        self.audits = self.register_child_endpoint(
            MarketingCampaignsIdAuditsEndpoint(client, parent_endpoint=self)
        )
        self.emailsOpened = self.register_child_endpoint(
            MarketingCampaignsIdEmailsOpenedEndpoint(client, parent_endpoint=self)
        )
        self.formsSubmitted = self.register_child_endpoint(
            MarketingCampaignsIdFormsSubmittedEndpoint(client, parent_endpoint=self)
        )
        self.linksClicked = self.register_child_endpoint(
            MarketingCampaignsIdLinksClickedEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> CampaignModel:
        return self._parse_one(CampaignModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> CampaignModel:
        return self._parse_one(CampaignModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> CampaignModel:
        return self._parse_one(CampaignModel, super().make_request("PATCH", params=params))
        