from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.FinanceCurrenciesIdEndpoint import FinanceCurrenciesIdEndpoint
from pywise.endpoints.manage.FinanceCurrenciesCountEndpoint import FinanceCurrenciesCountEndpoint
from pywise.endpoints.manage.FinanceCurrenciesInfoEndpoint import FinanceCurrenciesInfoEndpoint
from pywise.models.manage.CurrencyModel import CurrencyModel

class FinanceCurrenciesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "currencies", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceCurrenciesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceCurrenciesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceCurrenciesIdEndpoint:
        child = FinanceCurrenciesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CurrencyModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CurrencyModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CurrencyModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CurrencyModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CurrencyModel]: The parsed response data.
        """
        return self._parse_many(CurrencyModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CurrencyModel:
        """
        Performs a POST request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CurrencyModel: The parsed response data.
        """
        return self._parse_one(CurrencyModel, super().make_request("POST", params=params).json())
        