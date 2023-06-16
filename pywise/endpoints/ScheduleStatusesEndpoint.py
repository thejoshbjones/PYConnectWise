from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ScheduleStatusesIdEndpoint import ScheduleStatusesIdEndpoint
from pywise.endpoints.ScheduleStatusesCountEndpoint import ScheduleStatusesCountEndpoint
from pywise.models.ScheduleStatusModel import ScheduleStatusModel

class ScheduleStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleStatusesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ScheduleStatusesIdEndpoint:
        child = ScheduleStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ScheduleStatusModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ScheduleStatusModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ScheduleStatusModel]:
        return self._parse_many(ScheduleStatusModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ScheduleStatusModel:
        return self._parse_one(ScheduleStatusModel, super().make_request("POST", params=params))
        