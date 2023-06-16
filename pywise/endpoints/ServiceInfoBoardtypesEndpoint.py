from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceInfoBoardtypesIdEndpoint import ServiceInfoBoardtypesIdEndpoint
from pywise.endpoints.ServiceInfoBoardtypesCountEndpoint import ServiceInfoBoardtypesCountEndpoint
from pywise.models.BoardTypeInfoModel import BoardTypeInfoModel

class ServiceInfoBoardtypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "boardtypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceInfoBoardtypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceInfoBoardtypesIdEndpoint:
        child = ServiceInfoBoardtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardTypeInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardTypeInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardTypeInfoModel]:
        return self._parse_many(BoardTypeInfoModel, super().make_request("GET", params=params))
        