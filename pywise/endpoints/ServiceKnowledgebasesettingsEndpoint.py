from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceKnowledgebasesettingsIdEndpoint import ServiceKnowledgebasesettingsIdEndpoint
from pywise.models.KnowledgeBaseSettingsModel import KnowledgeBaseSettingsModel

class ServiceKnowledgebasesettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "knowledgebasesettings", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> ServiceKnowledgebasesettingsIdEndpoint:
        child = ServiceKnowledgebasesettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[KnowledgeBaseSettingsModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            KnowledgeBaseSettingsModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> KnowledgeBaseSettingsModel:
        return self._parse_one(KnowledgeBaseSettingsModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> KnowledgeBaseSettingsModel:
        return self._parse_one(KnowledgeBaseSettingsModel, super().make_request("POST", params=params))
        