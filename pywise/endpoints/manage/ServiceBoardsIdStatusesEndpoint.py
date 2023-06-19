from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServiceBoardsIdStatusesIdEndpoint import ServiceBoardsIdStatusesIdEndpoint
from pywise.endpoints.manage.ServiceBoardsIdStatusesCountEndpoint import ServiceBoardsIdStatusesCountEndpoint
from pywise.endpoints.manage.ServiceBoardsIdStatusesInfoEndpoint import ServiceBoardsIdStatusesInfoEndpoint
from pywise.models.manage.BoardStatusModel import BoardStatusModel

class ServiceBoardsIdStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceBoardsIdStatusesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceBoardsIdStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdStatusesIdEndpoint: The initialized ServiceBoardsIdStatusesIdEndpoint object.
        """
        child = ServiceBoardsIdStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardStatusModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardStatusModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BoardStatusModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardStatusModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardStatusModel]: The parsed response data.
        """
        return self._parse_many(BoardStatusModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardStatusModel:
        """
        Performs a POST request against the /service/boards/{parentId}/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardStatusModel: The parsed response data.
        """
        return self._parse_one(BoardStatusModel, super().make_request("POST", params=params).json())
        