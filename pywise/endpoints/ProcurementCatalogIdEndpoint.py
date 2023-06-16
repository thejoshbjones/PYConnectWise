from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementCatalogIdInfoEndpoint import ProcurementCatalogIdInfoEndpoint
from pywise.endpoints.ProcurementCatalogIdPricingEndpoint import ProcurementCatalogIdPricingEndpoint
from pywise.endpoints.ProcurementCatalogIdComponentsEndpoint import ProcurementCatalogIdComponentsEndpoint
from pywise.endpoints.ProcurementCatalogIdInventoryEndpoint import ProcurementCatalogIdInventoryEndpoint
from pywise.endpoints.ProcurementCatalogIdMinimumStockByWarehouseEndpoint import ProcurementCatalogIdMinimumStockByWarehouseEndpoint
from pywise.models.CatalogItemModel import CatalogItemModel

class ProcurementCatalogIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.info = self.register_child_endpoint(
            ProcurementCatalogIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.pricing = self.register_child_endpoint(
            ProcurementCatalogIdPricingEndpoint(client, parent_endpoint=self)
        )
        self.components = self.register_child_endpoint(
            ProcurementCatalogIdComponentsEndpoint(client, parent_endpoint=self)
        )
        self.inventory = self.register_child_endpoint(
            ProcurementCatalogIdInventoryEndpoint(client, parent_endpoint=self)
        )
        self.minimumStockByWarehouse = self.register_child_endpoint(
            ProcurementCatalogIdMinimumStockByWarehouseEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CatalogItemModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CatalogItemModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> CatalogItemModel:
        return self._parse_one(CatalogItemModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> CatalogItemModel:
        return self._parse_one(CatalogItemModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> CatalogItemModel:
        return self._parse_one(CatalogItemModel, super().make_request("PATCH", params=params))
        