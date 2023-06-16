from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemWorkflowsIdCopyEndpoint import SystemWorkflowsIdCopyEndpoint
from pywise.endpoints.SystemWorkflowsIdAttachmentsEndpoint import SystemWorkflowsIdAttachmentsEndpoint
from pywise.endpoints.SystemWorkflowsIdEventsEndpoint import SystemWorkflowsIdEventsEndpoint
from pywise.endpoints.SystemWorkflowsIdNotifyTypesEndpoint import SystemWorkflowsIdNotifyTypesEndpoint
from pywise.endpoints.SystemWorkflowsIdTriggersEndpoint import SystemWorkflowsIdTriggersEndpoint
from pywise.models.WorkflowModel import WorkflowModel

class SystemWorkflowsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
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
    
    def get(self, data=None, params=None) -> WorkflowModel:
        return self._parse_one(WorkflowModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> WorkflowModel:
        return self._parse_one(WorkflowModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> WorkflowModel:
        return self._parse_one(WorkflowModel, super().make_request("PATCH", params=params))
        