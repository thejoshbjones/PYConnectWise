from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ScheduleReminderTimesIdEndpoint import ScheduleReminderTimesIdEndpoint
from pywise.endpoints.ScheduleReminderTimesCountEndpoint import ScheduleReminderTimesCountEndpoint
from pywise.models.ScheduleReminderTimeModel import ScheduleReminderTimeModel

class ScheduleReminderTimesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "reminderTimes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleReminderTimesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ScheduleReminderTimesIdEndpoint:
        child = ScheduleReminderTimesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ScheduleReminderTimeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ScheduleReminderTimeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ScheduleReminderTimeModel]:
        return self._parse_many(ScheduleReminderTimeModel, super().make_request("GET", params=params))
        