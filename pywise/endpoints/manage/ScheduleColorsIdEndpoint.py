from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ScheduleColorsIdClearEndpoint import ScheduleColorsIdClearEndpoint
from pywise.models.manage.ScheduleColorModel import ScheduleColorModel

class ScheduleColorsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.clear = self.register_child_endpoint(
            ScheduleColorsIdClearEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ScheduleColorModel]:
        """
        Performs a GET request against the /schedule/colors/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleColorModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ScheduleColorModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ScheduleColorModel:
        """
        Performs a GET request against the /schedule/colors/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleColorModel: The parsed response data.
        """
        return self._parse_one(ScheduleColorModel, super().make_request("GET", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ScheduleColorModel:
        """
        Performs a PUT request against the /schedule/colors/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleColorModel: The parsed response data.
        """
        return self._parse_one(ScheduleColorModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ScheduleColorModel:
        """
        Performs a PATCH request against the /schedule/colors/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleColorModel: The parsed response data.
        """
        return self._parse_one(ScheduleColorModel, super().make_request("PATCH", params=params).json())
        