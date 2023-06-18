from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemWorkflowsIdNotifyTypesIdEndpoint import SystemWorkflowsIdNotifyTypesIdEndpoint
from pywise.endpoints.manage.SystemWorkflowsIdNotifyTypesCountEndpoint import SystemWorkflowsIdNotifyTypesCountEndpoint
from pywise.endpoints.manage.SystemWorkflowsIdNotifyTypesInfoEndpoint import SystemWorkflowsIdNotifyTypesInfoEndpoint
from pywise.models.manage.WorkflowNotifyTypeModel import WorkflowNotifyTypeModel

class SystemWorkflowsIdNotifyTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notifyTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemWorkflowsIdNotifyTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemWorkflowsIdNotifyTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemWorkflowsIdNotifyTypesIdEndpoint:
        child = SystemWorkflowsIdNotifyTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkflowNotifyTypeModel]:
        """
        Performs a GET request against the /system/workflows/{parentId}/notifyTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowNotifyTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkflowNotifyTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkflowNotifyTypeModel]:
        """
        Performs a GET request against the /system/workflows/{parentId}/notifyTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowNotifyTypeModel]: The parsed response data.
        """
        return self._parse_many(WorkflowNotifyTypeModel, super().make_request("GET", params=params).json())
        