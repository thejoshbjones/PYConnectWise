from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemWorkflowsIdCopyEndpoint import SystemWorkflowsIdCopyEndpoint
from pywise.endpoints.manage.SystemWorkflowsIdAttachmentsEndpoint import SystemWorkflowsIdAttachmentsEndpoint
from pywise.endpoints.manage.SystemWorkflowsIdEventsEndpoint import SystemWorkflowsIdEventsEndpoint
from pywise.endpoints.manage.SystemWorkflowsIdNotifyTypesEndpoint import SystemWorkflowsIdNotifyTypesEndpoint
from pywise.endpoints.manage.SystemWorkflowsIdTriggersEndpoint import SystemWorkflowsIdTriggersEndpoint
from pywise.models.manage.WorkflowModel import WorkflowModel

class SystemWorkflowsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.copy = self.register_child_endpoint(
            SystemWorkflowsIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.attachments = self.register_child_endpoint(
            SystemWorkflowsIdAttachmentsEndpoint(client, parent_endpoint=self)
        )
        self.events = self.register_child_endpoint(
            SystemWorkflowsIdEventsEndpoint(client, parent_endpoint=self)
        )
        self.notifyTypes = self.register_child_endpoint(
            SystemWorkflowsIdNotifyTypesEndpoint(client, parent_endpoint=self)
        )
        self.triggers = self.register_child_endpoint(
            SystemWorkflowsIdTriggersEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkflowModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkflowModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowModel:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowModel: The parsed response data.
        """
        return self._parse_one(WorkflowModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowModel:
        """
        Performs a PUT request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowModel: The parsed response data.
        """
        return self._parse_one(WorkflowModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowModel:
        """
        Performs a PATCH request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowModel: The parsed response data.
        """
        return self._parse_one(WorkflowModel, super().make_request("PATCH", params=params).json())
        