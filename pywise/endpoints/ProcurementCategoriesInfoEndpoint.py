from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementCategoriesInfoCountEndpoint import ProcurementCategoriesInfoCountEndpoint
from pywise.models.CategoryInfoModel import CategoryInfoModel

class ProcurementCategoriesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementCategoriesInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CategoryInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CategoryInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CategoryInfoModel]:
        return self._parse_many(CategoryInfoModel, super().make_request("GET", params=params))
        