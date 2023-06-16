from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMenuentriesIdEndpoint import SystemMenuentriesIdEndpoint
from pywise.endpoints.SystemMenuentriesCountEndpoint import SystemMenuentriesCountEndpoint
from pywise.models.MenuEntryModel import MenuEntryModel

class SystemMenuentriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "menuentries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMenuentriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMenuentriesIdEndpoint:
        child = SystemMenuentriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MenuEntryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MenuEntryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MenuEntryModel]:
        return self._parse_many(MenuEntryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MenuEntryModel:
        return self._parse_one(MenuEntryModel, super().make_request("POST", params=params))
        