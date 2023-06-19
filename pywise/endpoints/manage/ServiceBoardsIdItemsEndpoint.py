from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServiceBoardsIdItemsIdEndpoint import ServiceBoardsIdItemsIdEndpoint
from pywise.endpoints.manage.ServiceBoardsIdItemsCountEndpoint import ServiceBoardsIdItemsCountEndpoint
from pywise.models.manage.BoardItemModel import BoardItemModel

class ServiceBoardsIdItemsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "items", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdItemsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceBoardsIdItemsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdItemsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdItemsIdEndpoint: The initialized ServiceBoardsIdItemsIdEndpoint object.
        """
        child = ServiceBoardsIdItemsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardItemModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/items endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardItemModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BoardItemModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardItemModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/items endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardItemModel]: The parsed response data.
        """
        return self._parse_many(BoardItemModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardItemModel:
        """
        Performs a POST request against the /service/boards/{parentId}/items endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardItemModel: The parsed response data.
        """
        return self._parse_one(BoardItemModel, super().make_request("POST", params=params).json())
        