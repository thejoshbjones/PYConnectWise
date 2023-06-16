from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceTaxCodesIdTaxCodeLevelsIdEndpoint import FinanceTaxCodesIdTaxCodeLevelsIdEndpoint
from pywise.endpoints.FinanceTaxCodesIdTaxCodeLevelsCountEndpoint import FinanceTaxCodesIdTaxCodeLevelsCountEndpoint
from pywise.models.TaxCodeLevelModel import TaxCodeLevelModel

class FinanceTaxCodesIdTaxCodeLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxCodeLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdTaxCodeLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceTaxCodesIdTaxCodeLevelsIdEndpoint:
        child = FinanceTaxCodesIdTaxCodeLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TaxCodeLevelModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TaxCodeLevelModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TaxCodeLevelModel]:
        return self._parse_many(TaxCodeLevelModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TaxCodeLevelModel:
        return self._parse_one(TaxCodeLevelModel, super().make_request("POST", params=params))
        