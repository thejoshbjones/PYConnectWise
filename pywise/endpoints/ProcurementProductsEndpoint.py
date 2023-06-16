from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementProductsIdEndpoint import ProcurementProductsIdEndpoint
from pywise.endpoints.ProcurementProductsCountEndpoint import ProcurementProductsCountEndpoint
from pywise.models.ProductItemModel import ProductItemModel

class ProcurementProductsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "products", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementProductsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementProductsIdEndpoint:
        child = ProcurementProductsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProductItemModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProductItemModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProductItemModel]:
        return self._parse_many(ProductItemModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProductItemModel:
        return self._parse_one(ProductItemModel, super().make_request("POST", params=params))
        