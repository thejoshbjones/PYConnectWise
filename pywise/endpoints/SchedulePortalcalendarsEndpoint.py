from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SchedulePortalcalendarsIdEndpoint import SchedulePortalcalendarsIdEndpoint
from pywise.endpoints.SchedulePortalcalendarsCountEndpoint import SchedulePortalcalendarsCountEndpoint
from pywise.models.PortalCalendarModel import PortalCalendarModel

class SchedulePortalcalendarsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "portalcalendars", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SchedulePortalcalendarsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SchedulePortalcalendarsIdEndpoint:
        child = SchedulePortalcalendarsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PortalCalendarModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PortalCalendarModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PortalCalendarModel]:
        return self._parse_many(PortalCalendarModel, super().make_request("GET", params=params))
        