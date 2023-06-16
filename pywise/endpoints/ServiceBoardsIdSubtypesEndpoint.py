from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdSubtypesIdEndpoint import ServiceBoardsIdSubtypesIdEndpoint
from pywise.endpoints.ServiceBoardsIdSubtypesCountEndpoint import ServiceBoardsIdSubtypesCountEndpoint
from pywise.endpoints.ServiceBoardsIdSubtypesInfoEndpoint import ServiceBoardsIdSubtypesInfoEndpoint
from pywise.models.BoardSubTypeModel import BoardSubTypeModel

class ServiceBoardsIdSubtypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "subtypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdSubtypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceBoardsIdSubtypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdSubtypesIdEndpoint:
        child = ServiceBoardsIdSubtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardSubTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardSubTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardSubTypeModel]:
        return self._parse_many(BoardSubTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BoardSubTypeModel:
        return self._parse_one(BoardSubTypeModel, super().make_request("POST", params=params))
        