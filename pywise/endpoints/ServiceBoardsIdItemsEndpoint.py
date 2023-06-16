from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdItemsIdEndpoint import ServiceBoardsIdItemsIdEndpoint
from pywise.endpoints.ServiceBoardsIdItemsCountEndpoint import ServiceBoardsIdItemsCountEndpoint
from pywise.models.BoardItemModel import BoardItemModel

class ServiceBoardsIdItemsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "items", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdItemsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdItemsIdEndpoint:
        child = ServiceBoardsIdItemsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardItemModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardItemModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardItemModel]:
        return self._parse_many(BoardItemModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BoardItemModel:
        return self._parse_one(BoardItemModel, super().make_request("POST", params=params))
        