from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemWorkflowsTableTypesIdInfoEndpoint import SystemWorkflowsTableTypesIdInfoEndpoint
from pywise.models.WorkflowTableTypeModel import WorkflowTableTypeModel

class SystemWorkflowsTableTypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.info = self.register_child_endpoint(
            SystemWorkflowsTableTypesIdInfoEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> WorkflowTableTypeModel:
        return self._parse_one(WorkflowTableTypeModel, super().make_request("GET", params=params))
        