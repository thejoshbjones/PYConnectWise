from pywise.endpoints.base.connectwise_top_level_endpoint import ConnectWiseEndpoint

class ConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "configurations")
        