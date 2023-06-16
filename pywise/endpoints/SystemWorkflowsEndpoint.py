from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemWorkflowsIdEndpoint import SystemWorkflowsIdEndpoint
from pywise.endpoints.SystemWorkflowsCountEndpoint import SystemWorkflowsCountEndpoint
from pywise.endpoints.SystemWorkflowsTableTypesEndpoint import SystemWorkflowsTableTypesEndpoint
from pywise.models.WorkflowModel import WorkflowModel

class SystemWorkflowsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workflows", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemWorkflowsCountEndpoint(client, parent_endpoint=self)
        )
        self.tableTypes = self.register_child_endpoint(
            SystemWorkflowsTableTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemWorkflowsIdEndpoint:
        child = SystemWorkflowsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WorkflowModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WorkflowModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WorkflowModel]:
        return self._parse_many(WorkflowModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> WorkflowModel:
        return self._parse_one(WorkflowModel, super().make_request("POST", params=params))
        