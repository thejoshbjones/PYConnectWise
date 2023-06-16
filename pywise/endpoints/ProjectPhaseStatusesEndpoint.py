from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectPhaseStatusesIdEndpoint import ProjectPhaseStatusesIdEndpoint
from pywise.endpoints.ProjectPhaseStatusesCountEndpoint import ProjectPhaseStatusesCountEndpoint
from pywise.models.PhaseStatusModel import PhaseStatusModel

class ProjectPhaseStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "phaseStatuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectPhaseStatusesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectPhaseStatusesIdEndpoint:
        child = ProjectPhaseStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PhaseStatusModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PhaseStatusModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PhaseStatusModel]:
        return self._parse_many(PhaseStatusModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> PhaseStatusModel:
        return self._parse_one(PhaseStatusModel, super().make_request("POST", params=params))
        