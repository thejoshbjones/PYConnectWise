from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemConnectwisehostedsetupsIdEndpoint import SystemConnectwisehostedsetupsIdEndpoint
from pywise.endpoints.SystemConnectwisehostedsetupsCountEndpoint import SystemConnectwisehostedsetupsCountEndpoint
from pywise.models.ConnectWiseHostedSetupModel import ConnectWiseHostedSetupModel

class SystemConnectwisehostedsetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "connectwisehostedsetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemConnectwisehostedsetupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemConnectwisehostedsetupsIdEndpoint:
        child = SystemConnectwisehostedsetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ConnectWiseHostedSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ConnectWiseHostedSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ConnectWiseHostedSetupModel]:
        return self._parse_many(ConnectWiseHostedSetupModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ConnectWiseHostedSetupModel:
        return self._parse_one(ConnectWiseHostedSetupModel, super().make_request("POST", params=params))
        