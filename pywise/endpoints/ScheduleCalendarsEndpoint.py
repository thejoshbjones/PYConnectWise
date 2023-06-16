from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ScheduleCalendarsIdEndpoint import ScheduleCalendarsIdEndpoint
from pywise.endpoints.ScheduleCalendarsCountEndpoint import ScheduleCalendarsCountEndpoint
from pywise.endpoints.ScheduleCalendarsInfoEndpoint import ScheduleCalendarsInfoEndpoint
from pywise.models.CalendarModel import CalendarModel

class ScheduleCalendarsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "calendars", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleCalendarsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ScheduleCalendarsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ScheduleCalendarsIdEndpoint:
        child = ScheduleCalendarsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CalendarModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CalendarModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CalendarModel]:
        return self._parse_many(CalendarModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CalendarModel:
        return self._parse_one(CalendarModel, super().make_request("POST", params=params))
        