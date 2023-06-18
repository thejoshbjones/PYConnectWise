from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.FinanceInvoicesIdPaymentsIdEndpoint import FinanceInvoicesIdPaymentsIdEndpoint
from pywise.models.manage.PaymentModel import PaymentModel

class FinanceInvoicesIdPaymentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "payments", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> FinanceInvoicesIdPaymentsIdEndpoint:
        child = FinanceInvoicesIdPaymentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PaymentModel]:
        """
        Performs a GET request against the /finance/invoices/{parentId}/payments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PaymentModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PaymentModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PaymentModel]:
        """
        Performs a GET request against the /finance/invoices/{parentId}/payments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PaymentModel]: The parsed response data.
        """
        return self._parse_many(PaymentModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PaymentModel:
        """
        Performs a POST request against the /finance/invoices/{parentId}/payments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaymentModel: The parsed response data.
        """
        return self._parse_one(PaymentModel, super().make_request("POST", params=params).json())
        