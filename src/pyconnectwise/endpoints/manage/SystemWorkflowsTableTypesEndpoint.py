from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemWorkflowsTableTypesIdEndpoint import SystemWorkflowsTableTypesIdEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsTableTypesCountEndpoint import SystemWorkflowsTableTypesCountEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsTableTypesInfoEndpoint import SystemWorkflowsTableTypesInfoEndpoint
from pyconnectwise.models.manage.WorkflowTableTypeModel import WorkflowTableTypeModel

class SystemWorkflowsTableTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tableTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemWorkflowsTableTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemWorkflowsTableTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemWorkflowsTableTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsTableTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsTableTypesIdEndpoint: The initialized SystemWorkflowsTableTypesIdEndpoint object.
        """
        child = SystemWorkflowsTableTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkflowTableTypeModel]:
        """
        Performs a GET request against the /system/workflows/tableTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowTableTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkflowTableTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkflowTableTypeModel]:
        """
        Performs a GET request against the /system/workflows/tableTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowTableTypeModel]: The parsed response data.
        """
        return self._parse_many(WorkflowTableTypeModel, super().make_request("GET", params=params).json())
        