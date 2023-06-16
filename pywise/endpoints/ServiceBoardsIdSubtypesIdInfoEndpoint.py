from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.BoardSubTypeInfoModel import BoardSubTypeInfoModel

class ServiceBoardsIdSubtypesIdInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint, id_index="{id}")
        
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardSubTypeInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardSubTypeInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> BoardSubTypeInfoModel:
        return self._parse_one(BoardSubTypeInfoModel, super().make_request("GET", params=params))
        