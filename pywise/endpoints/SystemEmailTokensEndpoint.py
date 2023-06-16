from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemEmailTokensIdEndpoint import SystemEmailTokensIdEndpoint
from pywise.endpoints.SystemEmailTokensCountEndpoint import SystemEmailTokensCountEndpoint
from pywise.models.EmailTokenModel import EmailTokenModel

class SystemEmailTokensEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailTokens", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemEmailTokensCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemEmailTokensIdEndpoint:
        child = SystemEmailTokensIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[EmailTokenModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            EmailTokenModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[EmailTokenModel]:
        return self._parse_many(EmailTokenModel, super().make_request("GET", params=params))
        