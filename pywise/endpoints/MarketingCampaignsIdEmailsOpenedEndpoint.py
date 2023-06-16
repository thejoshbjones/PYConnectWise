from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.MarketingCampaignsIdEmailsOpenedIdEndpoint import MarketingCampaignsIdEmailsOpenedIdEndpoint
from pywise.endpoints.MarketingCampaignsIdEmailsOpenedCountEndpoint import MarketingCampaignsIdEmailsOpenedCountEndpoint
from pywise.models.EmailOpenedModel import EmailOpenedModel

class MarketingCampaignsIdEmailsOpenedEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailsOpened", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsIdEmailsOpenedCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> MarketingCampaignsIdEmailsOpenedIdEndpoint:
        child = MarketingCampaignsIdEmailsOpenedIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[EmailOpenedModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            EmailOpenedModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[EmailOpenedModel]:
        return self._parse_many(EmailOpenedModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> EmailOpenedModel:
        return self._parse_one(EmailOpenedModel, super().make_request("POST", params=params))
        