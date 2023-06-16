from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemTodayPageCategoriesIdEndpoint import SystemTodayPageCategoriesIdEndpoint
from pywise.endpoints.SystemTodayPageCategoriesCountEndpoint import SystemTodayPageCategoriesCountEndpoint
from pywise.models.TodayPageCategoryModel import TodayPageCategoryModel

class SystemTodayPageCategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "todayPageCategories", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemTodayPageCategoriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemTodayPageCategoriesIdEndpoint:
        child = SystemTodayPageCategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TodayPageCategoryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TodayPageCategoryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TodayPageCategoryModel]:
        return self._parse_many(TodayPageCategoryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TodayPageCategoryModel:
        return self._parse_one(TodayPageCategoryModel, super().make_request("POST", params=params))
        