from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ScheduleEntriesIdEndpoint import ScheduleEntriesIdEndpoint
from pywise.endpoints.ScheduleEntriesCountEndpoint import ScheduleEntriesCountEndpoint
from pywise.models.ScheduleEntryModel import ScheduleEntryModel

class ScheduleEntriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "entries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleEntriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ScheduleEntriesIdEndpoint:
        child = ScheduleEntriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ScheduleEntryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ScheduleEntryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ScheduleEntryModel]:
        return self._parse_many(ScheduleEntryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ScheduleEntryModel:
        return self._parse_one(ScheduleEntryModel, super().make_request("POST", params=params))
        