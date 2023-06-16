from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdAutoAssignResourcesIdEndpoint import ServiceBoardsIdAutoAssignResourcesIdEndpoint
from pywise.endpoints.ServiceBoardsIdAutoAssignResourcesCountEndpoint import ServiceBoardsIdAutoAssignResourcesCountEndpoint
from pywise.models.BoardAutoAssignResourceModel import BoardAutoAssignResourceModel

class ServiceBoardsIdAutoAssignResourcesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "autoAssignResources", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdAutoAssignResourcesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdAutoAssignResourcesIdEndpoint:
        child = ServiceBoardsIdAutoAssignResourcesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardAutoAssignResourceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardAutoAssignResourceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardAutoAssignResourceModel]:
        return self._parse_many(BoardAutoAssignResourceModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BoardAutoAssignResourceModel:
        return self._parse_one(BoardAutoAssignResourceModel, super().make_request("POST", params=params))
        