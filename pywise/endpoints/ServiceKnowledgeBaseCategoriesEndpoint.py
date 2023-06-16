from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceKnowledgeBaseCategoriesIdEndpoint import ServiceKnowledgeBaseCategoriesIdEndpoint
from pywise.endpoints.ServiceKnowledgeBaseCategoriesCountEndpoint import ServiceKnowledgeBaseCategoriesCountEndpoint
from pywise.models.KnowledgeBaseCategoryModel import KnowledgeBaseCategoryModel

class ServiceKnowledgeBaseCategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "knowledgeBaseCategories", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceKnowledgeBaseCategoriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceKnowledgeBaseCategoriesIdEndpoint:
        child = ServiceKnowledgeBaseCategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[KnowledgeBaseCategoryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            KnowledgeBaseCategoryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[KnowledgeBaseCategoryModel]:
        return self._parse_many(KnowledgeBaseCategoryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> KnowledgeBaseCategoryModel:
        return self._parse_one(KnowledgeBaseCategoryModel, super().make_request("POST", params=params))
        