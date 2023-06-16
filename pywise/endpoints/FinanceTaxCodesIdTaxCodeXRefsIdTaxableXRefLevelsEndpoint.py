from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsIdEndpoint import FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsIdEndpoint
from pywise.endpoints.FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsCountEndpoint import FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsCountEndpoint
from pywise.models.TaxableXRefLevelModel import TaxableXRefLevelModel

class FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableXRefLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsIdEndpoint:
        child = FinanceTaxCodesIdTaxCodeXRefsIdTaxableXRefLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TaxableXRefLevelModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TaxableXRefLevelModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TaxableXRefLevelModel]:
        return self._parse_many(TaxableXRefLevelModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TaxableXRefLevelModel:
        return self._parse_one(TaxableXRefLevelModel, super().make_request("POST", params=params))
        