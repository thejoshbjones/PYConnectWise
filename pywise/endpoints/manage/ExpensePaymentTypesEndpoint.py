from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ExpensePaymentTypesIdEndpoint import ExpensePaymentTypesIdEndpoint
from pywise.endpoints.manage.ExpensePaymentTypesCountEndpoint import ExpensePaymentTypesCountEndpoint
from pywise.endpoints.manage.ExpensePaymentTypesInfoEndpoint import ExpensePaymentTypesInfoEndpoint
from pywise.models.manage.PaymentTypeModel import PaymentTypeModel

class ExpensePaymentTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "paymentTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ExpensePaymentTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ExpensePaymentTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ExpensePaymentTypesIdEndpoint:
        child = ExpensePaymentTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PaymentTypeModel]:
        """
        Performs a GET request against the /expense/paymentTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PaymentTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PaymentTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PaymentTypeModel]:
        """
        Performs a GET request against the /expense/paymentTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PaymentTypeModel]: The parsed response data.
        """
        return self._parse_many(PaymentTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PaymentTypeModel:
        """
        Performs a POST request against the /expense/paymentTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaymentTypeModel: The parsed response data.
        """
        return self._parse_one(PaymentTypeModel, super().make_request("POST", params=params).json())
        