from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementPurchaseorderstatusesIdEmailtemplatesIdEndpoint import ProcurementPurchaseorderstatusesIdEmailtemplatesIdEndpoint
from pywise.endpoints.ProcurementPurchaseorderstatusesIdEmailtemplatesCountEndpoint import ProcurementPurchaseorderstatusesIdEmailtemplatesCountEndpoint
from pywise.models.PurchaseOrderStatusEmailTemplateModel import PurchaseOrderStatusEmailTemplateModel

class ProcurementPurchaseorderstatusesIdEmailtemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementPurchaseorderstatusesIdEmailtemplatesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementPurchaseorderstatusesIdEmailtemplatesIdEndpoint:
        child = ProcurementPurchaseorderstatusesIdEmailtemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PurchaseOrderStatusEmailTemplateModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PurchaseOrderStatusEmailTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PurchaseOrderStatusEmailTemplateModel]:
        return self._parse_many(PurchaseOrderStatusEmailTemplateModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> PurchaseOrderStatusEmailTemplateModel:
        return self._parse_one(PurchaseOrderStatusEmailTemplateModel, super().make_request("POST", params=params))
        