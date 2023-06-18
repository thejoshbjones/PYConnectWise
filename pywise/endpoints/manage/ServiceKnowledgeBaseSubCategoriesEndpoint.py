from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServiceKnowledgeBaseSubCategoriesIdEndpoint import ServiceKnowledgeBaseSubCategoriesIdEndpoint
from pywise.endpoints.manage.ServiceKnowledgeBaseSubCategoriesCountEndpoint import ServiceKnowledgeBaseSubCategoriesCountEndpoint
from pywise.models.manage.KnowledgeBaseSubCategoryModel import KnowledgeBaseSubCategoryModel

class ServiceKnowledgeBaseSubCategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "knowledgeBaseSubCategories", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceKnowledgeBaseSubCategoriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceKnowledgeBaseSubCategoriesIdEndpoint:
        child = ServiceKnowledgeBaseSubCategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[KnowledgeBaseSubCategoryModel]:
        """
        Performs a GET request against the /service/knowledgeBaseSubCategories endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[KnowledgeBaseSubCategoryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            KnowledgeBaseSubCategoryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[KnowledgeBaseSubCategoryModel]:
        """
        Performs a GET request against the /service/knowledgeBaseSubCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KnowledgeBaseSubCategoryModel]: The parsed response data.
        """
        return self._parse_many(KnowledgeBaseSubCategoryModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> KnowledgeBaseSubCategoryModel:
        """
        Performs a POST request against the /service/knowledgeBaseSubCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseSubCategoryModel: The parsed response data.
        """
        return self._parse_one(KnowledgeBaseSubCategoryModel, super().make_request("POST", params=params).json())
        