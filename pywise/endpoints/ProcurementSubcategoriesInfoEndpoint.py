from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementSubcategoriesInfoCountEndpoint import ProcurementSubcategoriesInfoCountEndpoint
from pywise.models.SubCategoryInfoModel import SubCategoryInfoModel

class ProcurementSubcategoriesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementSubcategoriesInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SubCategoryInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SubCategoryInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SubCategoryInfoModel]:
        return self._parse_many(SubCategoryInfoModel, super().make_request("GET", params=params))
        