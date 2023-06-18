from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProjectPhaseStatusesIdEndpoint import ProjectPhaseStatusesIdEndpoint
from pywise.endpoints.manage.ProjectPhaseStatusesCountEndpoint import ProjectPhaseStatusesCountEndpoint
from pywise.models.manage.PhaseStatusModel import PhaseStatusModel

class ProjectPhaseStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "phaseStatuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectPhaseStatusesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectPhaseStatusesIdEndpoint:
        child = ProjectPhaseStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PhaseStatusModel]:
        """
        Performs a GET request against the /project/phaseStatuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PhaseStatusModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PhaseStatusModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PhaseStatusModel]:
        """
        Performs a GET request against the /project/phaseStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PhaseStatusModel]: The parsed response data.
        """
        return self._parse_many(PhaseStatusModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PhaseStatusModel:
        """
        Performs a POST request against the /project/phaseStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PhaseStatusModel: The parsed response data.
        """
        return self._parse_one(PhaseStatusModel, super().make_request("POST", params=params).json())
        