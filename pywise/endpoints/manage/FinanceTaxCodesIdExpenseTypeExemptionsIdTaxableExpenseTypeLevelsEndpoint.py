from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.FinanceTaxCodesIdExpenseTypeExemptionsIdTaxableExpenseTypeLevelsIdEndpoint import FinanceTaxCodesIdExpenseTypeExemptionsIdTaxableExpenseTypeLevelsIdEndpoint
from pywise.endpoints.manage.FinanceTaxCodesIdExpenseTypeExemptionsIdTaxableExpenseTypeLevelsCountEndpoint import FinanceTaxCodesIdExpenseTypeExemptionsIdTaxableExpenseTypeLevelsCountEndpoint
from pywise.models.manage.TaxableExpenseTypeLevelModel import TaxableExpenseTypeLevelModel

class FinanceTaxCodesIdExpenseTypeExemptionsIdTaxableExpenseTypeLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableExpenseTypeLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdExpenseTypeExemptionsIdTaxableExpenseTypeLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceTaxCodesIdExpenseTypeExemptionsIdTaxableExpenseTypeLevelsIdEndpoint:
        child = FinanceTaxCodesIdExpenseTypeExemptionsIdTaxableExpenseTypeLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaxableExpenseTypeLevelModel]:
        """
        Performs a GET request against the /finance/taxCodes/{grandparentId}/expenseTypeExemptions/{parentId}/taxableExpenseTypeLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxableExpenseTypeLevelModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TaxableExpenseTypeLevelModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxableExpenseTypeLevelModel]:
        """
        Performs a GET request against the /finance/taxCodes/{grandparentId}/expenseTypeExemptions/{parentId}/taxableExpenseTypeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxableExpenseTypeLevelModel]: The parsed response data.
        """
        return self._parse_many(TaxableExpenseTypeLevelModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxableExpenseTypeLevelModel:
        """
        Performs a POST request against the /finance/taxCodes/{grandparentId}/expenseTypeExemptions/{parentId}/taxableExpenseTypeLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableExpenseTypeLevelModel: The parsed response data.
        """
        return self._parse_one(TaxableExpenseTypeLevelModel, super().make_request("POST", params=params).json())
        