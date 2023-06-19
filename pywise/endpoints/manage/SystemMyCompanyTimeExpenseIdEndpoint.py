from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.models.manage.TimeExpenseModel import TimeExpenseModel

class SystemMyCompanyTimeExpenseIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TimeExpenseModel]:
        """
        Performs a GET request against the /system/myCompany/timeExpense/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeExpenseModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TimeExpenseModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TimeExpenseModel:
        """
        Performs a GET request against the /system/myCompany/timeExpense/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeExpenseModel: The parsed response data.
        """
        return self._parse_one(TimeExpenseModel, super().make_request("GET", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TimeExpenseModel:
        """
        Performs a PUT request against the /system/myCompany/timeExpense/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeExpenseModel: The parsed response data.
        """
        return self._parse_one(TimeExpenseModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TimeExpenseModel:
        """
        Performs a PATCH request against the /system/myCompany/timeExpense/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeExpenseModel: The parsed response data.
        """
        return self._parse_one(TimeExpenseModel, super().make_request("PATCH", params=params).json())
        