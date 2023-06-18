from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemWorkflowActionsIdAutomateParametersIdEndpoint import SystemWorkflowActionsIdAutomateParametersIdEndpoint
from pywise.endpoints.manage.SystemWorkflowActionsIdAutomateParametersCountEndpoint import SystemWorkflowActionsIdAutomateParametersCountEndpoint
from pywise.models.manage.WorkflowActionAutomateParameterModel import WorkflowActionAutomateParameterModel

class SystemWorkflowActionsIdAutomateParametersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "automateParameters", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemWorkflowActionsIdAutomateParametersCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemWorkflowActionsIdAutomateParametersIdEndpoint:
        child = SystemWorkflowActionsIdAutomateParametersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkflowActionAutomateParameterModel]:
        """
        Performs a GET request against the /system/workflowActions/{parentId}/automateParameters endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowActionAutomateParameterModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkflowActionAutomateParameterModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkflowActionAutomateParameterModel]:
        """
        Performs a GET request against the /system/workflowActions/{parentId}/automateParameters endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowActionAutomateParameterModel]: The parsed response data.
        """
        return self._parse_many(WorkflowActionAutomateParameterModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowActionAutomateParameterModel:
        """
        Performs a POST request against the /system/workflowActions/{parentId}/automateParameters endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowActionAutomateParameterModel: The parsed response data.
        """
        return self._parse_one(WorkflowActionAutomateParameterModel, super().make_request("POST", params=params).json())
        