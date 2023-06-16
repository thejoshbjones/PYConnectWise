from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemWorkflowsIdTriggersCountEndpoint import SystemWorkflowsIdTriggersCountEndpoint
from pywise.models.WorkflowTriggerModel import WorkflowTriggerModel

class SystemWorkflowsIdTriggersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "triggers", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemWorkflowsIdTriggersCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WorkflowTriggerModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WorkflowTriggerModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WorkflowTriggerModel]:
        return self._parse_many(WorkflowTriggerModel, super().make_request("GET", params=params))
        