from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMenuEntriesIdLocationsIdEndpoint import SystemMenuEntriesIdLocationsIdEndpoint
from pywise.endpoints.SystemMenuEntriesIdLocationsCountEndpoint import SystemMenuEntriesIdLocationsCountEndpoint
from pywise.models.MenuEntryLocationModel import MenuEntryLocationModel

class SystemMenuEntriesIdLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMenuEntriesIdLocationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMenuEntriesIdLocationsIdEndpoint:
        child = SystemMenuEntriesIdLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MenuEntryLocationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MenuEntryLocationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MenuEntryLocationModel]:
        return self._parse_many(MenuEntryLocationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MenuEntryLocationModel:
        return self._parse_one(MenuEntryLocationModel, super().make_request("POST", params=params))
        