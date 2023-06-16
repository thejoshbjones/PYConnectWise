from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementWarehousesIdEndpoint import ProcurementWarehousesIdEndpoint
from pywise.endpoints.ProcurementWarehousesCountEndpoint import ProcurementWarehousesCountEndpoint
from pywise.endpoints.ProcurementWarehousesInfoEndpoint import ProcurementWarehousesInfoEndpoint
from pywise.models.WarehouseModel import WarehouseModel

class ProcurementWarehousesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "warehouses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementWarehousesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementWarehousesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementWarehousesIdEndpoint:
        child = ProcurementWarehousesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WarehouseModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WarehouseModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WarehouseModel]:
        return self._parse_many(WarehouseModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> WarehouseModel:
        return self._parse_one(WarehouseModel, super().make_request("POST", params=params))
        