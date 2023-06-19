from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.models.manage.WorkflowActionUserDefinedFieldModel import WorkflowActionUserDefinedFieldModel

class SystemWorkflowsUserdefinedfieldsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
    
    
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowActionUserDefinedFieldModel:
        """
        Performs a PUT request against the /system/workflows/userdefinedfields/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowActionUserDefinedFieldModel: The parsed response data.
        """
        return self._parse_one(WorkflowActionUserDefinedFieldModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowActionUserDefinedFieldModel:
        """
        Performs a PATCH request against the /system/workflows/userdefinedfields/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowActionUserDefinedFieldModel: The parsed response data.
        """
        return self._parse_one(WorkflowActionUserDefinedFieldModel, super().make_request("PATCH", params=params).json())
        