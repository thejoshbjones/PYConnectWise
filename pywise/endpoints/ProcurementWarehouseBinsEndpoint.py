from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementWarehouseBinsIdEndpoint import ProcurementWarehouseBinsIdEndpoint
from pywise.endpoints.ProcurementWarehouseBinsCountEndpoint import ProcurementWarehouseBinsCountEndpoint
from pywise.endpoints.ProcurementWarehouseBinsInfoEndpoint import ProcurementWarehouseBinsInfoEndpoint
from pywise.models.WarehouseBinModel import WarehouseBinModel

class ProcurementWarehouseBinsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "warehouseBins", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementWarehouseBinsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementWarehouseBinsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementWarehouseBinsIdEndpoint:
        child = ProcurementWarehouseBinsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
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
    
    def get(self, data=None, params=None) -> list[WarehouseBinModel]:
        return self._parse_many(WarehouseBinModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> WarehouseBinModel:
        return self._parse_one(WarehouseBinModel, super().make_request("POST", params=params))
        