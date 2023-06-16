from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemImapsIdEndpoint import SystemImapsIdEndpoint
from pywise.endpoints.SystemImapsCountEndpoint import SystemImapsCountEndpoint
from pywise.endpoints.SystemImapsInfoEndpoint import SystemImapsInfoEndpoint
from pywise.models.ImapModel import ImapModel

class SystemImapsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "imaps", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemImapsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemImapsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemImapsIdEndpoint:
        child = SystemImapsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ImapModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ImapModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ImapModel]:
        return self._parse_many(ImapModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ImapModel:
        return self._parse_one(ImapModel, super().make_request("POST", params=params))
        