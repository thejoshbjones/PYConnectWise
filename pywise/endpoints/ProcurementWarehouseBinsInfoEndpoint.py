from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementWarehouseBinsInfoCountEndpoint import ProcurementWarehouseBinsInfoCountEndpoint
from pywise.models.WarehouseBinInfoModel import WarehouseBinInfoModel

class ProcurementWarehouseBinsInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementWarehouseBinsInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WarehouseBinInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WarehouseBinInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WarehouseBinInfoModel]:
        return self._parse_many(WarehouseBinInfoModel, super().make_request("GET", params=params))
        