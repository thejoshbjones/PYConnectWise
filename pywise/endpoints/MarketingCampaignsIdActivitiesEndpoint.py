from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.MarketingCampaignsIdActivitiesCountEndpoint import MarketingCampaignsIdActivitiesCountEndpoint
from pywise.models.ActivityReferenceModel import ActivityReferenceModel

class MarketingCampaignsIdActivitiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "activities", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsIdActivitiesCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ActivityReferenceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ActivityReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ActivityReferenceModel]:
        return self._parse_many(ActivityReferenceModel, super().make_request("GET", params=params))
        