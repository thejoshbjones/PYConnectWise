from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceTaxCodesIdExpenseTypeExemptionsIdTaxableExpenseTypeLevelsIdEndpoint import FinanceTaxCodesIdExpenseTypeExemptionsIdTaxableExpenseTypeLevelsIdEndpoint
from pywise.endpoints.FinanceTaxCodesIdExpenseTypeExemptionsIdTaxableExpenseTypeLevelsCountEndpoint import FinanceTaxCodesIdExpenseTypeExemptionsIdTaxableExpenseTypeLevelsCountEndpoint
from pywise.models.TaxableExpenseTypeLevelModel import TaxableExpenseTypeLevelModel

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
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TaxableExpenseTypeLevelModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TaxableExpenseTypeLevelModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TaxableExpenseTypeLevelModel]:
        return self._parse_many(TaxableExpenseTypeLevelModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TaxableExpenseTypeLevelModel:
        return self._parse_one(TaxableExpenseTypeLevelModel, super().make_request("POST", params=params))
        