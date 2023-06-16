from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceKnowledgeBaseArticlesIdEndpoint import ServiceKnowledgeBaseArticlesIdEndpoint
from pywise.endpoints.ServiceKnowledgeBaseArticlesCountEndpoint import ServiceKnowledgeBaseArticlesCountEndpoint
from pywise.models.KnowledgeBaseArticleModel import KnowledgeBaseArticleModel

class ServiceKnowledgeBaseArticlesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "knowledgeBaseArticles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceKnowledgeBaseArticlesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceKnowledgeBaseArticlesIdEndpoint:
        child = ServiceKnowledgeBaseArticlesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[KnowledgeBaseArticleModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            KnowledgeBaseArticleModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[KnowledgeBaseArticleModel]:
        return self._parse_many(KnowledgeBaseArticleModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> KnowledgeBaseArticleModel:
        return self._parse_one(KnowledgeBaseArticleModel, super().make_request("POST", params=params))
        