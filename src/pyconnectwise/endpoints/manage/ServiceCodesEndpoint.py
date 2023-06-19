from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceCodesIdEndpoint import ServiceCodesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceCodesCountEndpoint import ServiceCodesCountEndpoint
from pyconnectwise.models.manage.CodeModel import CodeModel

class ServiceCodesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "codes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceCodesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceCodesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceCodesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceCodesIdEndpoint: The initialized ServiceCodesIdEndpoint object.
        """
        child = ServiceCodesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CodeModel]:
        """
        Performs a GET request against the /service/codes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CodeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CodeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CodeModel]:
        """
        Performs a GET request against the /service/codes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CodeModel]: The parsed response data.
        """
        return self._parse_many(CodeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CodeModel:
        """
        Performs a POST request against the /service/codes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CodeModel: The parsed response data.
        """
        return self._parse_one(CodeModel, super().make_request("POST", params=params).json())
        