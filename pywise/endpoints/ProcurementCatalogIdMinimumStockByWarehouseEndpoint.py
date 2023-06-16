from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementCatalogIdMinimumStockByWarehouseIdEndpoint import ProcurementCatalogIdMinimumStockByWarehouseIdEndpoint
from pywise.endpoints.ProcurementCatalogIdMinimumStockByWarehouseCountEndpoint import ProcurementCatalogIdMinimumStockByWarehouseCountEndpoint
from pywise.models.MinimumStockByWarehouseModel import MinimumStockByWarehouseModel

class ProcurementCatalogIdMinimumStockByWarehouseEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "minimumStockByWarehouse", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementCatalogIdMinimumStockByWarehouseCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementCatalogIdMinimumStockByWarehouseIdEndpoint:
        child = ProcurementCatalogIdMinimumStockByWarehouseIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MinimumStockByWarehouseModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MinimumStockByWarehouseModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MinimumStockByWarehouseModel]:
        return self._parse_many(MinimumStockByWarehouseModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MinimumStockByWarehouseModel:
        return self._parse_one(MinimumStockByWarehouseModel, super().make_request("POST", params=params))
        