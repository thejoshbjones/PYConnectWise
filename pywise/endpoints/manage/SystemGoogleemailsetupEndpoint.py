from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemGoogleemailsetupIdEndpoint import SystemGoogleemailsetupIdEndpoint
from pywise.endpoints.manage.SystemGoogleemailsetupCountEndpoint import SystemGoogleemailsetupCountEndpoint
from pywise.models.manage.GoogleEmailSetupModel import GoogleEmailSetupModel

class SystemGoogleemailsetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemGoogleemailsetupCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemGoogleemailsetupIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemGoogleemailsetupIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemGoogleemailsetupIdEndpoint: The initialized SystemGoogleemailsetupIdEndpoint object.
        """
        child = SystemGoogleemailsetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[GoogleEmailSetupModel]:
        """
        Performs a GET request against the /system/googleemailsetup/ endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[GoogleEmailSetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            GoogleEmailSetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[GoogleEmailSetupModel]:
        """
        Performs a GET request against the /system/googleemailsetup/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[GoogleEmailSetupModel]: The parsed response data.
        """
        return self._parse_many(GoogleEmailSetupModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GoogleEmailSetupModel:
        """
        Performs a POST request against the /system/googleemailsetup/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GoogleEmailSetupModel: The parsed response data.
        """
        return self._parse_one(GoogleEmailSetupModel, super().make_request("POST", params=params).json())
        