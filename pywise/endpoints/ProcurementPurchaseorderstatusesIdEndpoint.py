from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementPurchaseorderstatusesIdUsagesEndpoint import ProcurementPurchaseorderstatusesIdUsagesEndpoint
from pywise.endpoints.ProcurementPurchaseorderstatusesIdNotificationsEndpoint import ProcurementPurchaseorderstatusesIdNotificationsEndpoint
from pywise.models.PurchaseOrderStatusModel import PurchaseOrderStatusModel

class ProcurementPurchaseorderstatusesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.usages = self.register_child_endpoint(
            ProcurementPurchaseorderstatusesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.notifications = self.register_child_endpoint(
            ProcurementPurchaseorderstatusesIdNotificationsEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> PurchaseOrderStatusModel:
        return self._parse_one(PurchaseOrderStatusModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def patch(self, data=None, params=None) -> PurchaseOrderStatusModel:
        return self._parse_one(PurchaseOrderStatusModel, super().make_request("PATCH", params=params))
        
    def put(self, data=None, params=None) -> PurchaseOrderStatusModel:
        return self._parse_one(PurchaseOrderStatusModel, super().make_request("PUT", params=params))
        