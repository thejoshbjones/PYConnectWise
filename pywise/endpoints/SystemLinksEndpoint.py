from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemLinksIdEndpoint import SystemLinksIdEndpoint
from pywise.endpoints.SystemLinksCountEndpoint import SystemLinksCountEndpoint
from pywise.models.LinkModel import LinkModel

class SystemLinksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "links", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemLinksCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemLinksIdEndpoint:
        child = SystemLinksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[LinkModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            LinkModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[LinkModel]:
        return self._parse_many(LinkModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> LinkModel:
        return self._parse_one(LinkModel, super().make_request("POST", params=params))
        