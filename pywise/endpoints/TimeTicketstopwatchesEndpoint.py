from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeTicketstopwatchesIdEndpoint import TimeTicketstopwatchesIdEndpoint
from pywise.endpoints.TimeTicketstopwatchesCountEndpoint import TimeTicketstopwatchesCountEndpoint
from pywise.models.TicketStopwatchModel import TicketStopwatchModel

class TimeTicketstopwatchesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ticketstopwatches", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeTicketstopwatchesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeTicketstopwatchesIdEndpoint:
        child = TimeTicketstopwatchesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TicketStopwatchModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TicketStopwatchModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TicketStopwatchModel]:
        return self._parse_many(TicketStopwatchModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TicketStopwatchModel:
        return self._parse_one(TicketStopwatchModel, super().make_request("POST", params=params))
        