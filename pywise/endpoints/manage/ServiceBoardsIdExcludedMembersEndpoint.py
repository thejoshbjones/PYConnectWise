from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServiceBoardsIdExcludedMembersIdEndpoint import ServiceBoardsIdExcludedMembersIdEndpoint
from pywise.endpoints.manage.ServiceBoardsIdExcludedMembersCountEndpoint import ServiceBoardsIdExcludedMembersCountEndpoint
from pywise.models.manage.BoardExcludedMemberModel import BoardExcludedMemberModel

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
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardExcludedMemberModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/excludedMembers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardExcludedMemberModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BoardExcludedMemberModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardExcludedMemberModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/excludedMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardExcludedMemberModel]: The parsed response data.
        """
        return self._parse_many(BoardExcludedMemberModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardExcludedMemberModel:
        """
        Performs a POST request against the /service/boards/{parentId}/excludedMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardExcludedMemberModel: The parsed response data.
        """
        return self._parse_one(BoardExcludedMemberModel, super().make_request("POST", params=params).json())
        