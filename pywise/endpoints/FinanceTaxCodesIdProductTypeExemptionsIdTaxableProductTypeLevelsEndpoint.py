from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsIdEndpoint import FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsIdEndpoint
from pywise.endpoints.FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsCountEndpoint import FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsCountEndpoint
from pywise.models.TaxableProductTypeLevelModel import TaxableProductTypeLevelModel

class FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableProductTypeLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsIdEndpoint:
        child = FinanceTaxCodesIdProductTypeExemptionsIdTaxableProductTypeLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TaxableProductTypeLevelModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TaxableProductTypeLevelModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TaxableProductTypeLevelModel]:
        return self._parse_many(TaxableProductTypeLevelModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TaxableProductTypeLevelModel:
        return self._parse_one(TaxableProductTypeLevelModel, super().make_request("POST", params=params))
        