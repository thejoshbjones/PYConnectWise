from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeActivitystopwatchesIdEndpoint import TimeActivitystopwatchesIdEndpoint
from pywise.endpoints.TimeActivitystopwatchesCountEndpoint import TimeActivitystopwatchesCountEndpoint
from pywise.models.ActivityStopwatchModel import ActivityStopwatchModel

class TimeActivitystopwatchesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "activitystopwatches", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeActivitystopwatchesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeActivitystopwatchesIdEndpoint:
        child = TimeActivitystopwatchesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ActivityStopwatchModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ActivityStopwatchModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ActivityStopwatchModel]:
        return self._parse_many(ActivityStopwatchModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ActivityStopwatchModel:
        return self._parse_one(ActivityStopwatchModel, super().make_request("POST", params=params))
        