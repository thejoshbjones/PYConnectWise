from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.models.manage.UnpostedExpenseTaxableLevelModel import UnpostedExpenseTaxableLevelModel

class FinanceAccountingUnpostedexpensesIdTaxableLevelsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[UnpostedExpenseTaxableLevelModel]:
        """
        Performs a GET request against the /finance/accounting/unpostedexpenses/{parentId}/taxableLevels/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedExpenseTaxableLevelModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            UnpostedExpenseTaxableLevelModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> UnpostedExpenseTaxableLevelModel:
        """
        Performs a GET request against the /finance/accounting/unpostedexpenses/{parentId}/taxableLevels/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UnpostedExpenseTaxableLevelModel: The parsed response data.
        """
        return self._parse_one(UnpostedExpenseTaxableLevelModel, super().make_request("GET", params=params).json())
        