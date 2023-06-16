from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdEndpoint import ServiceBoardsIdEndpoint
from pywise.endpoints.ServiceBoardsCopyEndpoint import ServiceBoardsCopyEndpoint
from pywise.endpoints.ServiceBoardsCountEndpoint import ServiceBoardsCountEndpoint
from pywise.models.BoardModel import BoardModel

class ServiceBoardsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "boards", parent_endpoint=parent_endpoint)
        
        self.copy = self.register_child_endpoint(
            ServiceBoardsCopyEndpoint(client, parent_endpoint=self)
        )
        self.count = self.register_child_endpoint(
            ServiceBoardsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdEndpoint:
        child = ServiceBoardsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardModel]:
        return self._parse_many(BoardModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BoardModel:
        return self._parse_one(BoardModel, super().make_request("POST", params=params))
        