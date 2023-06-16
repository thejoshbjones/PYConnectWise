from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemSetupScreensIdEndpoint import SystemSetupScreensIdEndpoint
from pywise.endpoints.SystemSetupScreensCountEndpoint import SystemSetupScreensCountEndpoint
from pywise.models.SetupScreenModel import SetupScreenModel

class SystemSetupScreensEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "setupScreens", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemSetupScreensCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemSetupScreensIdEndpoint:
        child = SystemSetupScreensIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SetupScreenModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SetupScreenModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SetupScreenModel]:
        return self._parse_many(SetupScreenModel, super().make_request("GET", params=params))
        