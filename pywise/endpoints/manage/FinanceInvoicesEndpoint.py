from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.FinanceInvoicesIdEndpoint import FinanceInvoicesIdEndpoint
from pywise.endpoints.manage.FinanceInvoicesCountEndpoint import FinanceInvoicesCountEndpoint
from pywise.models.manage.InvoiceModel import InvoiceModel

class FinanceInvoicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "invoices", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceInvoicesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceInvoicesIdEndpoint:
        child = FinanceInvoicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[InvoiceModel]:
        """
        Performs a GET request against the /finance/invoices endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InvoiceModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            InvoiceModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[InvoiceModel]:
        """
        Performs a GET request against the /finance/invoices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InvoiceModel]: The parsed response data.
        """
        return self._parse_many(InvoiceModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> InvoiceModel:
        """
        Performs a POST request against the /finance/invoices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InvoiceModel: The parsed response data.
        """
        return self._parse_one(InvoiceModel, super().make_request("POST", params=params).json())
        