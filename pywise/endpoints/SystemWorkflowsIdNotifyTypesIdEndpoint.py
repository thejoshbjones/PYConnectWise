from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemWorkflowsIdNotifyTypesIdInfoEndpoint import SystemWorkflowsIdNotifyTypesIdInfoEndpoint
from pywise.models.WorkflowNotifyTypeModel import WorkflowNotifyTypeModel

class SystemWorkflowsIdNotifyTypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.info = self.register_child_endpoint(
            SystemWorkflowsIdNotifyTypesIdInfoEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> WorkflowNotifyTypeModel:
        return self._parse_one(WorkflowNotifyTypeModel, super().make_request("GET", params=params))
        