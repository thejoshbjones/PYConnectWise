from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceTaxCodesIdEndpoint import FinanceTaxCodesIdEndpoint
from pywise.endpoints.FinanceTaxCodesCountEndpoint import FinanceTaxCodesCountEndpoint
from pywise.endpoints.FinanceTaxCodesInfoEndpoint import FinanceTaxCodesInfoEndpoint
from pywise.models.TaxCodeModel import TaxCodeModel

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
    
    def get(self, data=None, params=None) -> list[TaxCodeModel]:
        return self._parse_many(TaxCodeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TaxCodeModel:
        return self._parse_one(TaxCodeModel, super().make_request("POST", params=params))
        