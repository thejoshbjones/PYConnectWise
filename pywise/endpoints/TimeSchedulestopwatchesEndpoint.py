from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeSchedulestopwatchesIdEndpoint import TimeSchedulestopwatchesIdEndpoint
from pywise.endpoints.TimeSchedulestopwatchesCountEndpoint import TimeSchedulestopwatchesCountEndpoint
from pywise.models.ScheduleStopwatchModel import ScheduleStopwatchModel

class TimeSchedulestopwatchesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "schedulestopwatches", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeSchedulestopwatchesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeSchedulestopwatchesIdEndpoint:
        child = TimeSchedulestopwatchesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ScheduleStopwatchModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ScheduleStopwatchModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ScheduleStopwatchModel]:
        return self._parse_many(ScheduleStopwatchModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ScheduleStopwatchModel:
        return self._parse_one(ScheduleStopwatchModel, super().make_request("POST", params=params))
        