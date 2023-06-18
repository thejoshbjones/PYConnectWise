from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ScheduleHolidayListsIdHolidaysIdEndpoint import ScheduleHolidayListsIdHolidaysIdEndpoint
from pywise.endpoints.manage.ScheduleHolidayListsIdHolidaysCountEndpoint import ScheduleHolidayListsIdHolidaysCountEndpoint
from pywise.models.manage.HolidayModel import HolidayModel

class ScheduleHolidayListsIdHolidaysEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "holidays", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleHolidayListsIdHolidaysCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ScheduleHolidayListsIdHolidaysIdEndpoint:
        child = ScheduleHolidayListsIdHolidaysIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[HolidayModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[HolidayModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            HolidayModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[HolidayModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[HolidayModel]: The parsed response data.
        """
        return self._parse_many(HolidayModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> HolidayModel:
        """
        Performs a POST request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            HolidayModel: The parsed response data.
        """
        return self._parse_one(HolidayModel, super().make_request("POST", params=params).json())
        