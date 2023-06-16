from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementCatalogIdInventoryIdEndpoint import ProcurementCatalogIdInventoryIdEndpoint
from pywise.endpoints.ProcurementCatalogIdInventoryCountEndpoint import ProcurementCatalogIdInventoryCountEndpoint
from pywise.models.CatalogInventoryModel import CatalogInventoryModel

class ProcurementCatalogIdInventoryEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "inventory", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementCatalogIdInventoryCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementCatalogIdInventoryIdEndpoint:
        child = ProcurementCatalogIdInventoryIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CatalogInventoryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CatalogInventoryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CatalogInventoryModel]:
        return self._parse_many(CatalogInventoryModel, super().make_request("GET", params=params))
        