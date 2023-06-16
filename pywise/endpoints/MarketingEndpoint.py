from pywise.endpoints.base.connectwise_top_level_endpoint import ConnectWiseEndpoint
from pywise.endpoints.MarketingCampaignsEndpoint import MarketingCampaignsEndpoint
from pywise.endpoints.MarketingGroupsEndpoint import MarketingGroupsEndpoint

class MarketingEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "marketing")
        
        self.campaigns = self.register_child_endpoint(
            MarketingCampaignsEndpoint(client, parent_endpoint=self)
        )
        self.groups = self.register_child_endpoint(
            MarketingGroupsEndpoint(client, parent_endpoint=self)
        )