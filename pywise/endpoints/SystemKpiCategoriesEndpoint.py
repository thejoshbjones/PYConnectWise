from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemKpiCategoriesIdEndpoint import SystemKpiCategoriesIdEndpoint
from pywise.endpoints.SystemKpiCategoriesCountEndpoint import SystemKpiCategoriesCountEndpoint
from pywise.models.KPICategoryModel import KPICategoryModel

class SystemKpiCategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "kpiCategories", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemKpiCategoriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemKpiCategoriesIdEndpoint:
        child = SystemKpiCategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[KPICategoryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            KPICategoryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[KPICategoryModel]:
        return self._parse_many(KPICategoryModel, super().make_request("GET", params=params))
        