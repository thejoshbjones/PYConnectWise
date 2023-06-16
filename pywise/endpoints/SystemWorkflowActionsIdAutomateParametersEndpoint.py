from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemWorkflowActionsIdAutomateParametersIdEndpoint import SystemWorkflowActionsIdAutomateParametersIdEndpoint
from pywise.endpoints.SystemWorkflowActionsIdAutomateParametersCountEndpoint import SystemWorkflowActionsIdAutomateParametersCountEndpoint
from pywise.models.WorkflowActionAutomateParameterModel import WorkflowActionAutomateParameterModel

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
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WorkflowActionAutomateParameterModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WorkflowActionAutomateParameterModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WorkflowActionAutomateParameterModel]:
        return self._parse_many(WorkflowActionAutomateParameterModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> WorkflowActionAutomateParameterModel:
        return self._parse_one(WorkflowActionAutomateParameterModel, super().make_request("POST", params=params))
        