from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementProductsIdDetachEndpoint import ProcurementProductsIdDetachEndpoint
from pywise.endpoints.ProcurementProductsIdComponentsEndpoint import ProcurementProductsIdComponentsEndpoint
from pywise.endpoints.ProcurementProductsIdPickingShippingDetailsEndpoint import ProcurementProductsIdPickingShippingDetailsEndpoint
from pywise.models.ProductItemModel import ProductItemModel

class ProcurementProductsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.detach = self.register_child_endpoint(
            ProcurementProductsIdDetachEndpoint(client, parent_endpoint=self)
        )
        self.components = self.register_child_endpoint(
            ProcurementProductsIdComponentsEndpoint(client, parent_endpoint=self)
        )
        self.pickingShippingDetails = self.register_child_endpoint(
            ProcurementProductsIdPickingShippingDetailsEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> ProductItemModel:
        return self._parse_one(ProductItemModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> ProductItemModel:
        return self._parse_one(ProductItemModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> ProductItemModel:
        return self._parse_one(ProductItemModel, super().make_request("PATCH", params=params))
        