from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemWorkflowsIdEventsIdEndpoint import SystemWorkflowsIdEventsIdEndpoint
from pywise.endpoints.SystemWorkflowsIdEventsCountEndpoint import SystemWorkflowsIdEventsCountEndpoint
from pywise.models.WorkflowEventModel import WorkflowEventModel

class SystemWorkflowsIdEventsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "events", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemWorkflowsIdEventsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemWorkflowsIdEventsIdEndpoint:
        child = SystemWorkflowsIdEventsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WorkflowEventModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WorkflowEventModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WorkflowEventModel]:
        return self._parse_many(WorkflowEventModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> WorkflowEventModel:
        return self._parse_one(WorkflowEventModel, super().make_request("POST", params=params))
        