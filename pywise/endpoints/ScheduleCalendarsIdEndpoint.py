from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ScheduleCalendarsIdCopyEndpoint import ScheduleCalendarsIdCopyEndpoint
from pywise.endpoints.ScheduleCalendarsIdInfoEndpoint import ScheduleCalendarsIdInfoEndpoint
from pywise.endpoints.ScheduleCalendarsIdUsagesEndpoint import ScheduleCalendarsIdUsagesEndpoint
from pywise.models.CalendarModel import CalendarModel

class ScheduleCalendarsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.copy = self.register_child_endpoint(
            ScheduleCalendarsIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ScheduleCalendarsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            ScheduleCalendarsIdUsagesEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> CalendarModel:
        return self._parse_one(CalendarModel, super().make_request("GET", params=params))
        
    def patch(self, data=None, params=None) -> CalendarModel:
        return self._parse_one(CalendarModel, super().make_request("PATCH", params=params))
        
    def put(self, data=None, params=None) -> CalendarModel:
        return self._parse_one(CalendarModel, super().make_request("PUT", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        