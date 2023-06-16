from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementWarehouseBinsIdInventoryOnHandIdEndpoint import ProcurementWarehouseBinsIdInventoryOnHandIdEndpoint
from pywise.endpoints.ProcurementWarehouseBinsIdInventoryOnHandCountEndpoint import ProcurementWarehouseBinsIdInventoryOnHandCountEndpoint
from pywise.models.InventoryOnHandModel import InventoryOnHandModel

class ProcurementWarehouseBinsIdInventoryOnHandEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "inventoryOnHand", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementWarehouseBinsIdInventoryOnHandCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementWarehouseBinsIdInventoryOnHandIdEndpoint:
        child = ProcurementWarehouseBinsIdInventoryOnHandIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[InventoryOnHandModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            InventoryOnHandModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[InventoryOnHandModel]:
        return self._parse_many(InventoryOnHandModel, super().make_request("GET", params=params))
        