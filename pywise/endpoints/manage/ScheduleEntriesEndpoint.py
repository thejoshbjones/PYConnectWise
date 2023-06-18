from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ScheduleEntriesIdEndpoint import ScheduleEntriesIdEndpoint
from pywise.endpoints.manage.ScheduleEntriesCountEndpoint import ScheduleEntriesCountEndpoint
from pywise.models.manage.ScheduleEntryModel import ScheduleEntryModel

class ScheduleEntriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "entries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleEntriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ScheduleEntriesIdEndpoint:
        child = ScheduleEntriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ScheduleEntryModel]:
        """
        Performs a GET request against the /schedule/entries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleEntryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ScheduleEntryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ScheduleEntryModel]:
        """
        Performs a GET request against the /schedule/entries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleEntryModel]: The parsed response data.
        """
        return self._parse_many(ScheduleEntryModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ScheduleEntryModel:
        """
        Performs a POST request against the /schedule/entries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleEntryModel: The parsed response data.
        """
        return self._parse_one(ScheduleEntryModel, super().make_request("POST", params=params).json())
        