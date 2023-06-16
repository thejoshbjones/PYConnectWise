from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceTaxCodesIdTaxCodeXRefsIdEndpoint import FinanceTaxCodesIdTaxCodeXRefsIdEndpoint
from pywise.endpoints.FinanceTaxCodesIdTaxCodeXRefsCountEndpoint import FinanceTaxCodesIdTaxCodeXRefsCountEndpoint
from pywise.models.TaxCodeXRefModel import TaxCodeXRefModel

class FinanceTaxCodesIdTaxCodeXRefsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxCodeXRefs", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdTaxCodeXRefsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceTaxCodesIdTaxCodeXRefsIdEndpoint:
        child = FinanceTaxCodesIdTaxCodeXRefsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TaxCodeXRefModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TaxCodeXRefModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TaxCodeXRefModel]:
        return self._parse_many(TaxCodeXRefModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TaxCodeXRefModel:
        return self._parse_one(TaxCodeXRefModel, super().make_request("POST", params=params))
        