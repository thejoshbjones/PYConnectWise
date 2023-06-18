from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemInOutTypesIdEndpoint import SystemInOutTypesIdEndpoint
from pywise.endpoints.manage.SystemInOutTypesCountEndpoint import SystemInOutTypesCountEndpoint
from pywise.endpoints.manage.SystemInOutTypesInfoEndpoint import SystemInOutTypesInfoEndpoint
from pywise.models.manage.InOutTypeModel import InOutTypeModel

class SystemInOutTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "inOutTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInOutTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemInOutTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemInOutTypesIdEndpoint:
        child = SystemInOutTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[InOutTypeModel]:
        """
        Performs a GET request against the /system/inOutTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InOutTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            InOutTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[InOutTypeModel]:
        """
        Performs a GET request against the /system/inOutTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InOutTypeModel]: The parsed response data.
        """
        return self._parse_many(InOutTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> InOutTypeModel:
        """
        Performs a POST request against the /system/inOutTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InOutTypeModel: The parsed response data.
        """
        return self._parse_one(InOutTypeModel, super().make_request("POST", params=params).json())
        