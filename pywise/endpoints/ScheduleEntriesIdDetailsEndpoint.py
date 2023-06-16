from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ScheduleEntriesIdDetailsIdEndpoint import ScheduleEntriesIdDetailsIdEndpoint
from pywise.endpoints.ScheduleEntriesIdDetailsCountEndpoint import ScheduleEntriesIdDetailsCountEndpoint
from pywise.models.ScheduleDetailModel import ScheduleDetailModel

class ScheduleEntriesIdDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "details", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleEntriesIdDetailsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ScheduleEntriesIdDetailsIdEndpoint:
        child = ScheduleEntriesIdDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ScheduleDetailModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ScheduleDetailModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ScheduleDetailModel]:
        return self._parse_many(ScheduleDetailModel, super().make_request("GET", params=params))
        