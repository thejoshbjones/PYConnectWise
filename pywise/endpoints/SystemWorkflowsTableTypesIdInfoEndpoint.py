from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.WorkflowTableTypeInfoModel import WorkflowTableTypeInfoModel

class SystemWorkflowsTableTypesIdInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint, id_index="{id}")
        
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WorkflowTableTypeInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WorkflowTableTypeInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> WorkflowTableTypeInfoModel:
        return self._parse_one(WorkflowTableTypeInfoModel, super().make_request("GET", params=params))
        