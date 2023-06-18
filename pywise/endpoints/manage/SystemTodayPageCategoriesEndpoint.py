from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemTodayPageCategoriesIdEndpoint import SystemTodayPageCategoriesIdEndpoint
from pywise.endpoints.manage.SystemTodayPageCategoriesCountEndpoint import SystemTodayPageCategoriesCountEndpoint
from pywise.models.manage.TodayPageCategoryModel import TodayPageCategoryModel

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
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TodayPageCategoryModel]:
        """
        Performs a GET request against the /system/todayPageCategories endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TodayPageCategoryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TodayPageCategoryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TodayPageCategoryModel]:
        """
        Performs a GET request against the /system/todayPageCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TodayPageCategoryModel]: The parsed response data.
        """
        return self._parse_many(TodayPageCategoryModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TodayPageCategoryModel:
        """
        Performs a POST request against the /system/todayPageCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TodayPageCategoryModel: The parsed response data.
        """
        return self._parse_one(TodayPageCategoryModel, super().make_request("POST", params=params).json())
        