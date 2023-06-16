from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeEntriesIdEndpoint import TimeEntriesIdEndpoint
from pywise.endpoints.TimeEntriesCountEndpoint import TimeEntriesCountEndpoint
from pywise.endpoints.TimeEntriesDefaultsEndpoint import TimeEntriesDefaultsEndpoint
from pywise.models.TimeEntryModel import TimeEntryModel

class TimeEntriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "entries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeEntriesCountEndpoint(client, parent_endpoint=self)
        )
        self.defaults = self.register_child_endpoint(
            TimeEntriesDefaultsEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeEntriesIdEndpoint:
        child = TimeEntriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TimeEntryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TimeEntryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TimeEntryModel]:
        return self._parse_many(TimeEntryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TimeEntryModel:
        return self._parse_one(TimeEntryModel, super().make_request("POST", params=params))
        