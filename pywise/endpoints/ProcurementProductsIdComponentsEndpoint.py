from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementProductsIdComponentsIdEndpoint import ProcurementProductsIdComponentsIdEndpoint
from pywise.endpoints.ProcurementProductsIdComponentsCountEndpoint import ProcurementProductsIdComponentsCountEndpoint
from pywise.models.ProductComponentModel import ProductComponentModel

class ProcurementProductsIdComponentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "components", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementProductsIdComponentsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementProductsIdComponentsIdEndpoint:
        child = ProcurementProductsIdComponentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProductComponentModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProductComponentModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProductComponentModel]:
        return self._parse_many(ProductComponentModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> list[ProductComponentModel]:
        return self._parse_many(ProductComponentModel, super().make_request("POST", params=params))
        