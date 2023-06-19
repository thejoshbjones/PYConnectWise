from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.models.manage.ProjectModel import ProjectModel

class SalesOpportunitiesIdConvertToProjectEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "convertToProject", parent_endpoint=parent_endpoint)
        
    
    
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectModel:
        """
        Performs a POST request against the /sales/opportunities/{id}/convertToProject endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectModel: The parsed response data.
        """
        return self._parse_one(ProjectModel, super().make_request("POST", params=params).json())
        