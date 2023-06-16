from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementPurchaseorderstatusesIdEndpoint import ProcurementPurchaseorderstatusesIdEndpoint
from pywise.endpoints.ProcurementPurchaseorderstatusesCountEndpoint import ProcurementPurchaseorderstatusesCountEndpoint
from pywise.models.PurchaseOrderStatusModel import PurchaseOrderStatusModel

class ProcurementPurchaseorderstatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "purchaseorderstatuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementPurchaseorderstatusesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementPurchaseorderstatusesIdEndpoint:
        child = ProcurementPurchaseorderstatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PurchaseOrderStatusModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PurchaseOrderStatusModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PurchaseOrderStatusModel]:
        return self._parse_many(PurchaseOrderStatusModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> PurchaseOrderStatusModel:
        return self._parse_one(PurchaseOrderStatusModel, super().make_request("POST", params=params))
        