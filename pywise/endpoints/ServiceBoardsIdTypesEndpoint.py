from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdTypesIdEndpoint import ServiceBoardsIdTypesIdEndpoint
from pywise.endpoints.ServiceBoardsIdTypesCountEndpoint import ServiceBoardsIdTypesCountEndpoint
from pywise.models.BoardTypeModel import BoardTypeModel

class ServiceBoardsIdTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdTypesIdEndpoint:
        child = ServiceBoardsIdTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardTypeModel]:
        return self._parse_many(BoardTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BoardTypeModel:
        return self._parse_one(BoardTypeModel, super().make_request("POST", params=params))
        