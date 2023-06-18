from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServiceSLAsIdEndpoint import ServiceSLAsIdEndpoint
from pywise.endpoints.manage.ServiceSLAsCountEndpoint import ServiceSLAsCountEndpoint
from pywise.models.manage.SLAModel import SLAModel

class ServiceSLAsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "SLAs", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceSLAsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceSLAsIdEndpoint:
        child = ServiceSLAsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SLAModel]:
        """
        Performs a GET request against the /service/SLAs endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SLAModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SLAModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SLAModel]:
        """
        Performs a GET request against the /service/SLAs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SLAModel]: The parsed response data.
        """
        return self._parse_many(SLAModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SLAModel:
        """
        Performs a POST request against the /service/SLAs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SLAModel: The parsed response data.
        """
        return self._parse_one(SLAModel, super().make_request("POST", params=params).json())
        