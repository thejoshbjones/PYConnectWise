from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServicePrioritiesIdEndpoint import ServicePrioritiesIdEndpoint
from pywise.endpoints.manage.ServicePrioritiesCountEndpoint import ServicePrioritiesCountEndpoint
from pywise.models.manage.PriorityModel import PriorityModel

class ServicePrioritiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "priorities", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServicePrioritiesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServicePrioritiesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServicePrioritiesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServicePrioritiesIdEndpoint: The initialized ServicePrioritiesIdEndpoint object.
        """
        child = ServicePrioritiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PriorityModel]:
        """
        Performs a GET request against the /service/priorities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PriorityModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PriorityModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PriorityModel]:
        """
        Performs a GET request against the /service/priorities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PriorityModel]: The parsed response data.
        """
        return self._parse_many(PriorityModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PriorityModel:
        """
        Performs a POST request against the /service/priorities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PriorityModel: The parsed response data.
        """
        return self._parse_one(PriorityModel, super().make_request("POST", params=params).json())
        