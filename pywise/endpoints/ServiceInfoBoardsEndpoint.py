from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceInfoBoardsIdEndpoint import ServiceInfoBoardsIdEndpoint
from pywise.endpoints.ServiceInfoBoardsCountEndpoint import ServiceInfoBoardsCountEndpoint
from pywise.models.BoardInfoModel import BoardInfoModel

class ServiceInfoBoardsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "boards", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceInfoBoardsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceInfoBoardsIdEndpoint:
        child = ServiceInfoBoardsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardInfoModel]:
        return self._parse_many(BoardInfoModel, super().make_request("GET", params=params))
        