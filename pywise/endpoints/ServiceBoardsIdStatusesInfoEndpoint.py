from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdStatusesInfoCountEndpoint import ServiceBoardsIdStatusesInfoCountEndpoint
from pywise.models.BoardStatusInfoModel import BoardStatusInfoModel

class ServiceBoardsIdStatusesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdStatusesInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardStatusInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardStatusInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardStatusInfoModel]:
        return self._parse_many(BoardStatusInfoModel, super().make_request("GET", params=params))
        