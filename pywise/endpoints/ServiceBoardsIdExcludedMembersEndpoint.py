from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdExcludedMembersIdEndpoint import ServiceBoardsIdExcludedMembersIdEndpoint
from pywise.endpoints.ServiceBoardsIdExcludedMembersCountEndpoint import ServiceBoardsIdExcludedMembersCountEndpoint
from pywise.models.BoardExcludedMemberModel import BoardExcludedMemberModel

class ServiceBoardsIdExcludedMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "excludedMembers", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdExcludedMembersCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdExcludedMembersIdEndpoint:
        child = ServiceBoardsIdExcludedMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardExcludedMemberModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardExcludedMemberModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardExcludedMemberModel]:
        return self._parse_many(BoardExcludedMemberModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BoardExcludedMemberModel:
        return self._parse_one(BoardExcludedMemberModel, super().make_request("POST", params=params))
        