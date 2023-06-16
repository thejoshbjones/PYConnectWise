from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.ScheduleReminderTimeModel import ScheduleReminderTimeModel

class ScheduleReminderTimesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
    
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
    
    def get(self, data=None, params=None) -> ScheduleReminderTimeModel:
        return self._parse_one(ScheduleReminderTimeModel, super().make_request("GET", params=params))
        
    def put(self, data=None, params=None) -> ScheduleReminderTimeModel:
        return self._parse_one(ScheduleReminderTimeModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> ScheduleReminderTimeModel:
        return self._parse_one(ScheduleReminderTimeModel, super().make_request("PATCH", params=params))
        