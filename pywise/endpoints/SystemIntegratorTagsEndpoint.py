from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemIntegratorTagsIdEndpoint import SystemIntegratorTagsIdEndpoint
from pywise.endpoints.SystemIntegratorTagsCountEndpoint import SystemIntegratorTagsCountEndpoint
from pywise.models.IntegratorTagModel import IntegratorTagModel

class SystemIntegratorTagsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "integratorTags", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemIntegratorTagsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemIntegratorTagsIdEndpoint:
        child = SystemIntegratorTagsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[IntegratorTagModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            IntegratorTagModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[IntegratorTagModel]:
        return self._parse_many(IntegratorTagModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> IntegratorTagModel:
        return self._parse_one(IntegratorTagModel, super().make_request("POST", params=params))
        