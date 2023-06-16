from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementCategoriesIdEndpoint import ProcurementCategoriesIdEndpoint
from pywise.endpoints.ProcurementCategoriesCountEndpoint import ProcurementCategoriesCountEndpoint
from pywise.endpoints.ProcurementCategoriesInfoEndpoint import ProcurementCategoriesInfoEndpoint
from pywise.models.CategoryModel import CategoryModel

class ProcurementCategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "categories", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementCategoriesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementCategoriesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementCategoriesIdEndpoint:
        child = ProcurementCategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CategoryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CategoryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CategoryModel]:
        return self._parse_many(CategoryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CategoryModel:
        return self._parse_one(CategoryModel, super().make_request("POST", params=params))
        