from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.TimeTimePeriodSetupsIdEndpoint import TimeTimePeriodSetupsIdEndpoint
from pywise.endpoints.manage.TimeTimePeriodSetupsCountEndpoint import TimeTimePeriodSetupsCountEndpoint
from pywise.endpoints.manage.TimeTimePeriodSetupsDefaultEndpoint import TimeTimePeriodSetupsDefaultEndpoint
from pywise.models.manage.TimePeriodSetupModel import TimePeriodSetupModel

class TimeTimePeriodSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "timePeriodSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeTimePeriodSetupsCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self.register_child_endpoint(
            TimeTimePeriodSetupsDefaultEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeTimePeriodSetupsIdEndpoint:
        child = TimeTimePeriodSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TimePeriodSetupModel]:
        """
        Performs a GET request against the /time/timePeriodSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimePeriodSetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TimePeriodSetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TimePeriodSetupModel]:
        """
        Performs a GET request against the /time/timePeriodSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimePeriodSetupModel]: The parsed response data.
        """
        return self._parse_many(TimePeriodSetupModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TimePeriodSetupModel:
        """
        Performs a POST request against the /time/timePeriodSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimePeriodSetupModel: The parsed response data.
        """
        return self._parse_one(TimePeriodSetupModel, super().make_request("POST", params=params).json())
        