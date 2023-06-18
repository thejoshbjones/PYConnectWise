from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.TimeSheetsIdApproveEndpoint import TimeSheetsIdApproveEndpoint
from pywise.endpoints.manage.TimeSheetsIdRejectEndpoint import TimeSheetsIdRejectEndpoint
from pywise.endpoints.manage.TimeSheetsIdReverseEndpoint import TimeSheetsIdReverseEndpoint
from pywise.endpoints.manage.TimeSheetsIdSubmitEndpoint import TimeSheetsIdSubmitEndpoint
from pywise.endpoints.manage.TimeSheetsIdAuditsEndpoint import TimeSheetsIdAuditsEndpoint
from pywise.models.manage.TimeSheetModel import TimeSheetModel

class TimeSheetsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.approve = self.register_child_endpoint(
            TimeSheetsIdApproveEndpoint(client, parent_endpoint=self)
        )
        self.reject = self.register_child_endpoint(
            TimeSheetsIdRejectEndpoint(client, parent_endpoint=self)
        )
        self.reverse = self.register_child_endpoint(
            TimeSheetsIdReverseEndpoint(client, parent_endpoint=self)
        )
        self.submit = self.register_child_endpoint(
            TimeSheetsIdSubmitEndpoint(client, parent_endpoint=self)
        )
        self.audits = self.register_child_endpoint(
            TimeSheetsIdAuditsEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TimeSheetModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeSheetModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TimeSheetModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TimeSheetModel:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeSheetModel: The parsed response data.
        """
        return self._parse_one(TimeSheetModel, super().make_request("GET", params=params).json())
        