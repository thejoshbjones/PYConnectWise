from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementShipmentmethodsIdEndpoint import ProcurementShipmentmethodsIdEndpoint
from pywise.endpoints.ProcurementShipmentmethodsCountEndpoint import ProcurementShipmentmethodsCountEndpoint
from pywise.endpoints.ProcurementShipmentmethodsInfoEndpoint import ProcurementShipmentmethodsInfoEndpoint
from pywise.models.ShipmentMethodModel import ShipmentMethodModel

class ProcurementShipmentmethodsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "shipmentmethods", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementShipmentmethodsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementShipmentmethodsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementShipmentmethodsIdEndpoint:
        child = ProcurementShipmentmethodsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ShipmentMethodModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ShipmentMethodModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ShipmentMethodModel]:
        return self._parse_many(ShipmentMethodModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ShipmentMethodModel:
        return self._parse_one(ShipmentMethodModel, super().make_request("POST", params=params))
        