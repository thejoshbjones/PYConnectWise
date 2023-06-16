from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementPurchaseordersIdLineitemsIdEndpoint import ProcurementPurchaseordersIdLineitemsIdEndpoint
from pywise.endpoints.ProcurementPurchaseordersIdLineitemsBulkEndpoint import ProcurementPurchaseordersIdLineitemsBulkEndpoint
from pywise.endpoints.ProcurementPurchaseordersIdLineitemsCountEndpoint import ProcurementPurchaseordersIdLineitemsCountEndpoint
from pywise.models.PurchaseOrderLineItemModel import PurchaseOrderLineItemModel

class ProcurementPurchaseordersIdLineitemsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "lineitems", parent_endpoint=parent_endpoint)
        
        self.bulk = self.register_child_endpoint(
            ProcurementPurchaseordersIdLineitemsBulkEndpoint(client, parent_endpoint=self)
        )
        self.count = self.register_child_endpoint(
            ProcurementPurchaseordersIdLineitemsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementPurchaseordersIdLineitemsIdEndpoint:
        child = ProcurementPurchaseordersIdLineitemsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PurchaseOrderLineItemModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PurchaseOrderLineItemModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PurchaseOrderLineItemModel]:
        return self._parse_many(PurchaseOrderLineItemModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> PurchaseOrderLineItemModel:
        return self._parse_one(PurchaseOrderLineItemModel, super().make_request("POST", params=params))
        