from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsIdEndpoint import FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsIdEndpoint
from pywise.endpoints.manage.FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsCountEndpoint import FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsCountEndpoint
from pywise.models.manage.TaxableXRefLevelModel import TaxableXRefLevelModel

class FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableXRefLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsIdEndpoint: The initialized FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsIdEndpoint object.
        """
        child = FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaxableXRefLevelModel]:
        """
        Performs a GET request against the /finance/taxCodes/{grandparentId}/taxCodeXRefs/{parentId}/taxableXRefLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxableXRefLevelModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TaxableXRefLevelModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxableXRefLevelModel]:
        """
        Performs a GET request against the /finance/taxCodes/{grandparentId}/taxCodeXRefs/{parentId}/taxableXRefLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxableXRefLevelModel]: The parsed response data.
        """
        return self._parse_many(TaxableXRefLevelModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TaxableXRefLevelModel:
        """
        Performs a POST request against the /finance/taxCodes/{grandparentId}/taxCodeXRefs/{parentId}/taxableXRefLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TaxableXRefLevelModel: The parsed response data.
        """
        return self._parse_one(TaxableXRefLevelModel, super().make_request("POST", params=params).json())
        