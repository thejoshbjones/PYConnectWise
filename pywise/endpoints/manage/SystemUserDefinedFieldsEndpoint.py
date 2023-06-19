from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemUserDefinedFieldsIdEndpoint import SystemUserDefinedFieldsIdEndpoint
from pywise.endpoints.manage.SystemUserDefinedFieldsCountEndpoint import SystemUserDefinedFieldsCountEndpoint
from pywise.endpoints.manage.SystemUserDefinedFieldsInfoEndpoint import SystemUserDefinedFieldsInfoEndpoint
from pywise.models.manage.UserDefinedFieldModel import UserDefinedFieldModel

class SystemUserDefinedFieldsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "userDefinedFields", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemUserDefinedFieldsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemUserDefinedFieldsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemUserDefinedFieldsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemUserDefinedFieldsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemUserDefinedFieldsIdEndpoint: The initialized SystemUserDefinedFieldsIdEndpoint object.
        """
        child = SystemUserDefinedFieldsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[UserDefinedFieldModel]:
        """
        Performs a GET request against the /system/userDefinedFields endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UserDefinedFieldModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            UserDefinedFieldModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[UserDefinedFieldModel]:
        """
        Performs a GET request against the /system/userDefinedFields endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UserDefinedFieldModel]: The parsed response data.
        """
        return self._parse_many(UserDefinedFieldModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> UserDefinedFieldModel:
        """
        Performs a POST request against the /system/userDefinedFields endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UserDefinedFieldModel: The parsed response data.
        """
        return self._parse_one(UserDefinedFieldModel, super().make_request("POST", params=params).json())
        