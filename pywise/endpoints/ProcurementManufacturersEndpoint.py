from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementManufacturersIdEndpoint import ProcurementManufacturersIdEndpoint
from pywise.endpoints.ProcurementManufacturersCountEndpoint import ProcurementManufacturersCountEndpoint
from pywise.endpoints.ProcurementManufacturersInfoEndpoint import ProcurementManufacturersInfoEndpoint
from pywise.models.ManufacturerModel import ManufacturerModel

class ProcurementManufacturersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "manufacturers", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementManufacturersCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementManufacturersInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementManufacturersIdEndpoint:
        child = ProcurementManufacturersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManufacturerModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManufacturerModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManufacturerModel]:
        return self._parse_many(ManufacturerModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ManufacturerModel:
        return self._parse_one(ManufacturerModel, super().make_request("POST", params=params))
        