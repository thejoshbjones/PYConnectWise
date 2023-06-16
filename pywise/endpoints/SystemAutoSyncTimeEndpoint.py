from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemAutoSyncTimeIdEndpoint import SystemAutoSyncTimeIdEndpoint
from pywise.endpoints.SystemAutoSyncTimeCountEndpoint import SystemAutoSyncTimeCountEndpoint
from pywise.models.AutoSyncTimeModel import AutoSyncTimeModel

class SystemAutoSyncTimeEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "autoSyncTime", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemAutoSyncTimeCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemAutoSyncTimeIdEndpoint:
        child = SystemAutoSyncTimeIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AutoSyncTimeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AutoSyncTimeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AutoSyncTimeModel]:
        return self._parse_many(AutoSyncTimeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AutoSyncTimeModel:
        return self._parse_one(AutoSyncTimeModel, super().make_request("POST", params=params))
        