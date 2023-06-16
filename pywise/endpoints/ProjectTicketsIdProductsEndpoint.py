from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectTicketsIdProductsCountEndpoint import ProjectTicketsIdProductsCountEndpoint
from pywise.models.ProductReferenceModel import ProductReferenceModel

class ProjectTicketsIdProductsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "products", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectTicketsIdProductsCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProductReferenceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProductReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProductReferenceModel]:
        return self._parse_many(ProductReferenceModel, super().make_request("GET", params=params))
        