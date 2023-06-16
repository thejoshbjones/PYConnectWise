from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdTeamsIdEndpoint import ServiceBoardsIdTeamsIdEndpoint
from pywise.endpoints.ServiceBoardsIdTeamsCountEndpoint import ServiceBoardsIdTeamsCountEndpoint
from pywise.endpoints.ServiceBoardsIdTeamsInfoEndpoint import ServiceBoardsIdTeamsInfoEndpoint
from pywise.models.BoardTeamModel import BoardTeamModel

class ServiceBoardsIdTeamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teams", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdTeamsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceBoardsIdTeamsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdTeamsIdEndpoint:
        child = ServiceBoardsIdTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardTeamModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardTeamModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardTeamModel]:
        return self._parse_many(BoardTeamModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BoardTeamModel:
        return self._parse_one(BoardTeamModel, super().make_request("POST", params=params))
        