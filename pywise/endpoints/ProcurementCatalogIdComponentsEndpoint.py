from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementCatalogIdComponentsIdEndpoint import ProcurementCatalogIdComponentsIdEndpoint
from pywise.endpoints.ProcurementCatalogIdComponentsCountEndpoint import ProcurementCatalogIdComponentsCountEndpoint
from pywise.models.CatalogComponentModel import CatalogComponentModel

class ProcurementCatalogIdComponentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "components", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementCatalogIdComponentsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementCatalogIdComponentsIdEndpoint:
        child = ProcurementCatalogIdComponentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CatalogComponentModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CatalogComponentModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CatalogComponentModel]:
        return self._parse_many(CatalogComponentModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CatalogComponentModel:
        return self._parse_one(CatalogComponentModel, super().make_request("POST", params=params))
        