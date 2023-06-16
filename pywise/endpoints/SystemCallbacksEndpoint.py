from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemCallbacksIdEndpoint import SystemCallbacksIdEndpoint
from pywise.endpoints.SystemCallbacksCountEndpoint import SystemCallbacksCountEndpoint
from pywise.models.CallbackEntryModel import CallbackEntryModel

class SystemCallbacksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "callbacks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemCallbacksCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemCallbacksIdEndpoint:
        child = SystemCallbacksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CallbackEntryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CallbackEntryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CallbackEntryModel]:
        return self._parse_many(CallbackEntryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CallbackEntryModel:
        return self._parse_one(CallbackEntryModel, super().make_request("POST", params=params))
        