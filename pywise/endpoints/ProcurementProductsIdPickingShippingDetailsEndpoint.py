from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementProductsIdPickingShippingDetailsIdEndpoint import ProcurementProductsIdPickingShippingDetailsIdEndpoint
from pywise.endpoints.ProcurementProductsIdPickingShippingDetailsCountEndpoint import ProcurementProductsIdPickingShippingDetailsCountEndpoint
from pywise.models.ProductPickingShippingDetailModel import ProductPickingShippingDetailModel

class ProcurementProductsIdPickingShippingDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "pickingShippingDetails", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementProductsIdPickingShippingDetailsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementProductsIdPickingShippingDetailsIdEndpoint:
        child = ProcurementProductsIdPickingShippingDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProductPickingShippingDetailModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProductPickingShippingDetailModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProductPickingShippingDetailModel]:
        return self._parse_many(ProductPickingShippingDetailModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> list[ProductPickingShippingDetailModel]:
        return self._parse_many(ProductPickingShippingDetailModel, super().make_request("POST", params=params))
        