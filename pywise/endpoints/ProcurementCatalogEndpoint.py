from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementCatalogIdEndpoint import ProcurementCatalogIdEndpoint
from pywise.endpoints.ProcurementCatalogCountEndpoint import ProcurementCatalogCountEndpoint
from pywise.endpoints.ProcurementCatalogInfoEndpoint import ProcurementCatalogInfoEndpoint
from pywise.models.CatalogItemModel import CatalogItemModel

class ProcurementCatalogEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "catalog", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementCatalogCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementCatalogInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementCatalogIdEndpoint:
        child = ProcurementCatalogIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CatalogItemModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CatalogItemModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CatalogItemModel]:
        return self._parse_many(CatalogItemModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CatalogItemModel:
        return self._parse_one(CatalogItemModel, super().make_request("POST", params=params))
        