from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemWorkflowsTableTypesIdEndpoint import SystemWorkflowsTableTypesIdEndpoint
from pywise.endpoints.manage.SystemWorkflowsTableTypesCountEndpoint import SystemWorkflowsTableTypesCountEndpoint
from pywise.endpoints.manage.SystemWorkflowsTableTypesInfoEndpoint import SystemWorkflowsTableTypesInfoEndpoint
from pywise.models.manage.WorkflowTableTypeModel import WorkflowTableTypeModel

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
        child = SystemWorkflowsTableTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkflowTableTypeModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

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
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowTableTypeModel]: The parsed response data.
        """
        return self._parse_many(WorkflowTableTypeModel, super().make_request("GET", params=params).json())
        