from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceKnowledgeBaseSubCategoriesIdEndpoint import ServiceKnowledgeBaseSubCategoriesIdEndpoint
from pywise.endpoints.ServiceKnowledgeBaseSubCategoriesCountEndpoint import ServiceKnowledgeBaseSubCategoriesCountEndpoint
from pywise.models.KnowledgeBaseSubCategoryModel import KnowledgeBaseSubCategoryModel

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
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[KnowledgeBaseSubCategoryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            KnowledgeBaseSubCategoryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[KnowledgeBaseSubCategoryModel]:
        return self._parse_many(KnowledgeBaseSubCategoryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> KnowledgeBaseSubCategoryModel:
        return self._parse_one(KnowledgeBaseSubCategoryModel, super().make_request("POST", params=params))
        