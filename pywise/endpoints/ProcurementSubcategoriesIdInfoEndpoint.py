from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.SubCategoryInfoModel import SubCategoryInfoModel

class ProcurementSubcategoriesIdInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint, id_index="{id}")
        
    
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
    
    def get(self, data=None, params=None) -> SubCategoryInfoModel:
        return self._parse_one(SubCategoryInfoModel, super().make_request("GET", params=params))
        