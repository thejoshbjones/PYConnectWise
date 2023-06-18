from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemQuoteLinkSetupIdEndpoint import SystemQuoteLinkSetupIdEndpoint
from pywise.endpoints.manage.SystemQuoteLinkSetupCountEndpoint import SystemQuoteLinkSetupCountEndpoint
from pywise.endpoints.manage.SystemQuoteLinkSetupTestConnectionEndpoint import SystemQuoteLinkSetupTestConnectionEndpoint
from pywise.models.manage.QuoteLinkModel import QuoteLinkModel

class SystemQuoteLinkSetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "quoteLinkSetup", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemQuoteLinkSetupCountEndpoint(client, parent_endpoint=self)
        )
        self.testConnection = self.register_child_endpoint(
            SystemQuoteLinkSetupTestConnectionEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemQuoteLinkSetupIdEndpoint:
        child = SystemQuoteLinkSetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[QuoteLinkModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[QuoteLinkModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            QuoteLinkModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[QuoteLinkModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[QuoteLinkModel]: The parsed response data.
        """
        return self._parse_many(QuoteLinkModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> QuoteLinkModel:
        """
        Performs a POST request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            QuoteLinkModel: The parsed response data.
        """
        return self._parse_one(QuoteLinkModel, super().make_request("POST", params=params).json())
        