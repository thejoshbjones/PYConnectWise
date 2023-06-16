from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemInOutBoardsIdEndpoint import SystemInOutBoardsIdEndpoint
from pywise.endpoints.SystemInOutBoardsCountEndpoint import SystemInOutBoardsCountEndpoint
from pywise.models.InOutBoardModel import InOutBoardModel

class SystemInOutBoardsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "inOutBoards", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInOutBoardsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemInOutBoardsIdEndpoint:
        child = SystemInOutBoardsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[InOutBoardModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            InOutBoardModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[InOutBoardModel]:
        return self._parse_many(InOutBoardModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> InOutBoardModel:
        return self._parse_one(InOutBoardModel, super().make_request("POST", params=params))
        