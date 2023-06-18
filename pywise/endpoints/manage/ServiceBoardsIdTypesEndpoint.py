from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServiceBoardsIdTypesIdEndpoint import ServiceBoardsIdTypesIdEndpoint
from pywise.endpoints.manage.ServiceBoardsIdTypesCountEndpoint import ServiceBoardsIdTypesCountEndpoint
from pywise.models.manage.BoardTypeModel import BoardTypeModel

class ServiceBoardsIdTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdTypesIdEndpoint:
        child = ServiceBoardsIdTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardTypeModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BoardTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardTypeModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardTypeModel]: The parsed response data.
        """
        return self._parse_many(BoardTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardTypeModel:
        """
        Performs a POST request against the /service/boards/{parentId}/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardTypeModel: The parsed response data.
        """
        return self._parse_one(BoardTypeModel, super().make_request("POST", params=params).json())
        