from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementCategoriesIdSubcategoriesIdEndpoint import ProcurementCategoriesIdSubcategoriesIdEndpoint
from pywise.endpoints.ProcurementCategoriesIdSubcategoriesCountEndpoint import ProcurementCategoriesIdSubcategoriesCountEndpoint
from pywise.endpoints.ProcurementCategoriesIdSubcategoriesInfoEndpoint import ProcurementCategoriesIdSubcategoriesInfoEndpoint
from pywise.models.LegacySubCategoryModel import LegacySubCategoryModel

class ProcurementCategoriesIdSubcategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementCategoriesIdSubcategoriesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementCategoriesIdSubcategoriesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementCategoriesIdSubcategoriesIdEndpoint:
        child = ProcurementCategoriesIdSubcategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[LegacySubCategoryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            LegacySubCategoryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[LegacySubCategoryModel]:
        return self._parse_many(LegacySubCategoryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> LegacySubCategoryModel:
        return self._parse_one(LegacySubCategoryModel, super().make_request("POST", params=params))
        