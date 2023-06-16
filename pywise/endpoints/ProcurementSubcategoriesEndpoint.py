from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementSubcategoriesIdEndpoint import ProcurementSubcategoriesIdEndpoint
from pywise.endpoints.ProcurementSubcategoriesCountEndpoint import ProcurementSubcategoriesCountEndpoint
from pywise.models.SubCategoryModel import SubCategoryModel

class ProcurementSubcategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementSubcategoriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementSubcategoriesIdEndpoint:
        child = ProcurementSubcategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SubCategoryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SubCategoryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SubCategoryModel]:
        return self._parse_many(SubCategoryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SubCategoryModel:
        return self._parse_one(SubCategoryModel, super().make_request("POST", params=params))
        