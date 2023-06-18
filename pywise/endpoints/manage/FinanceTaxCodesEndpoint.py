from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.FinanceTaxCodesIdEndpoint import FinanceTaxCodesIdEndpoint
from pywise.endpoints.manage.FinanceTaxCodesCountEndpoint import FinanceTaxCodesCountEndpoint
from pywise.endpoints.manage.FinanceTaxCodesInfoEndpoint import FinanceTaxCodesInfoEndpoint
from pywise.models.manage.TaxCodeModel import TaxCodeModel

class FinanceTaxCodesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxCodes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceTaxCodesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceTaxCodesIdEndpoint:
        child = FinanceTaxCodesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaxCodeModel]:
        """
        Performs a GET request against the /finance/taxCodes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxCodeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TaxCodeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxCodeModel]:
        """
        Performs a GET request against the /finance/taxCodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxCodeModel]: The parsed response data.
        """
        return self._parse_many(TaxCodeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxCodeModel:
        """
        Performs a POST request against the /finance/taxCodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxCodeModel: The parsed response data.
        """
        return self._parse_one(TaxCodeModel, super().make_request("POST", params=params).json())
        