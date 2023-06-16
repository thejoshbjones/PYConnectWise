from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemWorkflowsTableTypesIdEndpoint import SystemWorkflowsTableTypesIdEndpoint
from pywise.endpoints.SystemWorkflowsTableTypesCountEndpoint import SystemWorkflowsTableTypesCountEndpoint
from pywise.endpoints.SystemWorkflowsTableTypesInfoEndpoint import SystemWorkflowsTableTypesInfoEndpoint
from pywise.models.WorkflowTableTypeModel import WorkflowTableTypeModel

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
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WorkflowTableTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WorkflowTableTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WorkflowTableTypeModel]:
        return self._parse_many(WorkflowTableTypeModel, super().make_request("GET", params=params))
        