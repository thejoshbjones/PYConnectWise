from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceTaxCodesIdProductTypeExemptionsIdEndpoint import FinanceTaxCodesIdProductTypeExemptionsIdEndpoint
from pywise.endpoints.FinanceTaxCodesIdProductTypeExemptionsCountEndpoint import FinanceTaxCodesIdProductTypeExemptionsCountEndpoint
from pywise.models.ProductTypeExemptionModel import ProductTypeExemptionModel

class FinanceTaxCodesIdProductTypeExemptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "productTypeExemptions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdProductTypeExemptionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceTaxCodesIdProductTypeExemptionsIdEndpoint:
        child = FinanceTaxCodesIdProductTypeExemptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProductTypeExemptionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProductTypeExemptionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProductTypeExemptionModel]:
        return self._parse_many(ProductTypeExemptionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProductTypeExemptionModel:
        return self._parse_one(ProductTypeExemptionModel, super().make_request("POST", params=params))
        