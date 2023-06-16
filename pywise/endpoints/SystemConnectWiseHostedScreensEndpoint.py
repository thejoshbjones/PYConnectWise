from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemConnectWiseHostedScreensIdEndpoint import SystemConnectWiseHostedScreensIdEndpoint
from pywise.endpoints.SystemConnectWiseHostedScreensCountEndpoint import SystemConnectWiseHostedScreensCountEndpoint
from pywise.models.ConnectWiseHostedScreenModel import ConnectWiseHostedScreenModel

class SystemConnectWiseHostedScreensEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "connectWiseHostedScreens", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemConnectWiseHostedScreensCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemConnectWiseHostedScreensIdEndpoint:
        child = SystemConnectWiseHostedScreensIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ConnectWiseHostedScreenModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ConnectWiseHostedScreenModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ConnectWiseHostedScreenModel]:
        return self._parse_many(ConnectWiseHostedScreenModel, super().make_request("GET", params=params))
        