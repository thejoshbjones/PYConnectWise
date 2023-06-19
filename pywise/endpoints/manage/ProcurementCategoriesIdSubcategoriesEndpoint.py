from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProcurementCategoriesIdSubcategoriesIdEndpoint import ProcurementCategoriesIdSubcategoriesIdEndpoint
from pywise.endpoints.manage.ProcurementCategoriesIdSubcategoriesCountEndpoint import ProcurementCategoriesIdSubcategoriesCountEndpoint
from pywise.endpoints.manage.ProcurementCategoriesIdSubcategoriesInfoEndpoint import ProcurementCategoriesIdSubcategoriesInfoEndpoint
from pywise.models.manage.LegacySubCategoryModel import LegacySubCategoryModel

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
        """
        Sets the ID for this endpoint and returns an initialized ProcurementCategoriesIdSubcategoriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementCategoriesIdSubcategoriesIdEndpoint: The initialized ProcurementCategoriesIdSubcategoriesIdEndpoint object.
        """
        child = ProcurementCategoriesIdSubcategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[LegacySubCategoryModel]:
        """
        Performs a GET request against the /procurement/categories/{parentId}/subcategories/ endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LegacySubCategoryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            LegacySubCategoryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LegacySubCategoryModel]:
        """
        Performs a GET request against the /procurement/categories/{parentId}/subcategories/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LegacySubCategoryModel]: The parsed response data.
        """
        return self._parse_many(LegacySubCategoryModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LegacySubCategoryModel:
        """
        Performs a POST request against the /procurement/categories/{parentId}/subcategories/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LegacySubCategoryModel: The parsed response data.
        """
        return self._parse_one(LegacySubCategoryModel, super().make_request("POST", params=params).json())
        