from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceTaxCodesIdCopyEndpoint import FinanceTaxCodesIdCopyEndpoint
from pywise.endpoints.FinanceTaxCodesIdInfoEndpoint import FinanceTaxCodesIdInfoEndpoint
from pywise.endpoints.FinanceTaxCodesIdUsagesEndpoint import FinanceTaxCodesIdUsagesEndpoint
from pywise.endpoints.FinanceTaxCodesIdExpenseTypeExemptionsEndpoint import FinanceTaxCodesIdExpenseTypeExemptionsEndpoint
from pywise.endpoints.FinanceTaxCodesIdProductTypeExemptionsEndpoint import FinanceTaxCodesIdProductTypeExemptionsEndpoint
from pywise.endpoints.FinanceTaxCodesIdTaxCodeLevelsEndpoint import FinanceTaxCodesIdTaxCodeLevelsEndpoint
from pywise.endpoints.FinanceTaxCodesIdTaxCodeXRefsEndpoint import FinanceTaxCodesIdTaxCodeXRefsEndpoint
from pywise.endpoints.FinanceTaxCodesIdWorkRoleExemptionsEndpoint import FinanceTaxCodesIdWorkRoleExemptionsEndpoint
from pywise.models.TaxCodeModel import TaxCodeModel

class FinanceTaxCodesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.copy = self.register_child_endpoint(
            FinanceTaxCodesIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceTaxCodesIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            FinanceTaxCodesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.expenseTypeExemptions = self.register_child_endpoint(
            FinanceTaxCodesIdExpenseTypeExemptionsEndpoint(client, parent_endpoint=self)
        )
        self.productTypeExemptions = self.register_child_endpoint(
            FinanceTaxCodesIdProductTypeExemptionsEndpoint(client, parent_endpoint=self)
        )
        self.taxCodeLevels = self.register_child_endpoint(
            FinanceTaxCodesIdTaxCodeLevelsEndpoint(client, parent_endpoint=self)
        )
        self.taxCodeXRefs = self.register_child_endpoint(
            FinanceTaxCodesIdTaxCodeXRefsEndpoint(client, parent_endpoint=self)
        )
        self.workRoleExemptions = self.register_child_endpoint(
            FinanceTaxCodesIdWorkRoleExemptionsEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TaxCodeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TaxCodeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> TaxCodeModel:
        return self._parse_one(TaxCodeModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> TaxCodeModel:
        return self._parse_one(TaxCodeModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> TaxCodeModel:
        return self._parse_one(TaxCodeModel, super().make_request("PATCH", params=params))
        