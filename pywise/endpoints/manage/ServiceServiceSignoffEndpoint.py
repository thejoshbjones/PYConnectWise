from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServiceServiceSignoffIdEndpoint import ServiceServiceSignoffIdEndpoint
from pywise.endpoints.manage.ServiceServiceSignoffCountEndpoint import ServiceServiceSignoffCountEndpoint
from pywise.endpoints.manage.ServiceServiceSignoffInfoEndpoint import ServiceServiceSignoffInfoEndpoint
from pywise.models.manage.ServiceSignoffModel import ServiceSignoffModel

class ServiceServiceSignoffEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "serviceSignoff", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceServiceSignoffCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceServiceSignoffInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceServiceSignoffIdEndpoint:
        child = ServiceServiceSignoffIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceSignoffModel]:
        """
        Performs a GET request against the /service/serviceSignoff endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceSignoffModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ServiceSignoffModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceSignoffModel]:
        """
        Performs a GET request against the /service/serviceSignoff endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceSignoffModel]: The parsed response data.
        """
        return self._parse_many(ServiceSignoffModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSignoffModel:
        """
        Performs a POST request against the /service/serviceSignoff endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSignoffModel: The parsed response data.
        """
        return self._parse_one(ServiceSignoffModel, super().make_request("POST", params=params).json())
        