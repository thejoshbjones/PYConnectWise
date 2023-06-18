from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SchedulePortalcalendarsIdEndpoint import SchedulePortalcalendarsIdEndpoint
from pywise.endpoints.manage.SchedulePortalcalendarsCountEndpoint import SchedulePortalcalendarsCountEndpoint
from pywise.models.manage.PortalCalendarModel import PortalCalendarModel

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
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PortalCalendarModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalCalendarModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PortalCalendarModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PortalCalendarModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalCalendarModel]: The parsed response data.
        """
        return self._parse_many(PortalCalendarModel, super().make_request("GET", params=params).json())
        