from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceTeamsIdEndpoint import ServiceTeamsIdEndpoint
from pywise.endpoints.ServiceTeamsCountEndpoint import ServiceTeamsCountEndpoint
from pywise.models.ServiceTeamModel import ServiceTeamModel

class ServiceTeamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teams", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTeamsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceTeamsIdEndpoint:
        child = ServiceTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ServiceTeamModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ServiceTeamModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ServiceTeamModel]:
        return self._parse_many(ServiceTeamModel, super().make_request("GET", params=params))
        