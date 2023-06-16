from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementWarehousesInfoCountEndpoint import ProcurementWarehousesInfoCountEndpoint
from pywise.models.WarehouseInfoModel import WarehouseInfoModel

class ProcurementWarehousesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementWarehousesInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WarehouseInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WarehouseInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WarehouseInfoModel]:
        return self._parse_many(WarehouseInfoModel, super().make_request("GET", params=params))
        