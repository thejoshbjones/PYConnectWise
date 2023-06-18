from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProjectProjectsIdPhasesIdEndpoint import ProjectProjectsIdPhasesIdEndpoint
from pywise.endpoints.manage.ProjectProjectsIdPhasesCountEndpoint import ProjectProjectsIdPhasesCountEndpoint
from pywise.models.manage.ProjectPhaseModel import ProjectPhaseModel

class ProjectProjectsIdPhasesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "phases", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectProjectsIdPhasesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectProjectsIdPhasesIdEndpoint:
        child = ProjectProjectsIdPhasesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectPhaseModel]:
        """
        Performs a GET request against the /project/projects/{parentId}/phases endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectPhaseModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProjectPhaseModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectPhaseModel]:
        """
        Performs a GET request against the /project/projects/{parentId}/phases endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectPhaseModel]: The parsed response data.
        """
        return self._parse_many(ProjectPhaseModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectPhaseModel:
        """
        Performs a POST request against the /project/projects/{parentId}/phases endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectPhaseModel: The parsed response data.
        """
        return self._parse_one(ProjectPhaseModel, super().make_request("POST", params=params).json())
        