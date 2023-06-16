from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemIntegratorloginsIdEndpoint import SystemIntegratorloginsIdEndpoint
from pywise.endpoints.SystemIntegratorloginsCountEndpoint import SystemIntegratorloginsCountEndpoint
from pywise.models.IntegratorLoginModel import IntegratorLoginModel

class SystemIntegratorloginsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "integratorlogins", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemIntegratorloginsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemIntegratorloginsIdEndpoint:
        child = SystemIntegratorloginsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[IntegratorLoginModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            IntegratorLoginModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[IntegratorLoginModel]:
        return self._parse_many(IntegratorLoginModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> IntegratorLoginModel:
        return self._parse_one(IntegratorLoginModel, super().make_request("POST", params=params))
        