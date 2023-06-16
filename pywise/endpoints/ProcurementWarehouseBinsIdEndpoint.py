from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementWarehouseBinsIdInfoEndpoint import ProcurementWarehouseBinsIdInfoEndpoint
from pywise.endpoints.ProcurementWarehouseBinsIdInventoryOnHandEndpoint import ProcurementWarehouseBinsIdInventoryOnHandEndpoint
from pywise.models.WarehouseBinModel import WarehouseBinModel

class ProcurementWarehouseBinsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.info = self.register_child_endpoint(
            ProcurementWarehouseBinsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.inventoryOnHand = self.register_child_endpoint(
            ProcurementWarehouseBinsIdInventoryOnHandEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WarehouseBinModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WarehouseBinModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> WarehouseBinModel:
        return self._parse_one(WarehouseBinModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> WarehouseBinModel:
        return self._parse_one(WarehouseBinModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> WarehouseBinModel:
        return self._parse_one(WarehouseBinModel, super().make_request("PATCH", params=params))
        