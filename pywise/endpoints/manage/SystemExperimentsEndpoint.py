from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemExperimentsIdEndpoint import SystemExperimentsIdEndpoint
from pywise.endpoints.manage.SystemExperimentsCountEndpoint import SystemExperimentsCountEndpoint
from pywise.models.manage.ExperimentModel import ExperimentModel

class SystemExperimentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "experiments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemExperimentsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemExperimentsIdEndpoint:
        child = SystemExperimentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ExperimentModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExperimentModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ExperimentModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ExperimentModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExperimentModel]: The parsed response data.
        """
        return self._parse_many(ExperimentModel, super().make_request("GET", params=params).json())
        