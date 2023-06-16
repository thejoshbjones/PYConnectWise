from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdStatusesIdEndpoint import ServiceBoardsIdStatusesIdEndpoint
from pywise.endpoints.ServiceBoardsIdStatusesCountEndpoint import ServiceBoardsIdStatusesCountEndpoint
from pywise.endpoints.ServiceBoardsIdStatusesInfoEndpoint import ServiceBoardsIdStatusesInfoEndpoint
from pywise.models.BoardStatusModel import BoardStatusModel

class ServiceBoardsIdStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceBoardsIdStatusesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdStatusesIdEndpoint:
        child = ServiceBoardsIdStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardStatusModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardStatusModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardStatusModel]:
        return self._parse_many(BoardStatusModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BoardStatusModel:
        return self._parse_one(BoardStatusModel, super().make_request("POST", params=params))
        