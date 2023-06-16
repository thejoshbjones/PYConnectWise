from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemWorkflowsIdNotifyTypesIdEndpoint import SystemWorkflowsIdNotifyTypesIdEndpoint
from pywise.endpoints.SystemWorkflowsIdNotifyTypesCountEndpoint import SystemWorkflowsIdNotifyTypesCountEndpoint
from pywise.endpoints.SystemWorkflowsIdNotifyTypesInfoEndpoint import SystemWorkflowsIdNotifyTypesInfoEndpoint
from pywise.models.WorkflowNotifyTypeModel import WorkflowNotifyTypeModel

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
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WorkflowNotifyTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WorkflowNotifyTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WorkflowNotifyTypeModel]:
        return self._parse_many(WorkflowNotifyTypeModel, super().make_request("GET", params=params))
        