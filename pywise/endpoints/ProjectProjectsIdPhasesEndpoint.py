from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectProjectsIdPhasesIdEndpoint import ProjectProjectsIdPhasesIdEndpoint
from pywise.endpoints.ProjectProjectsIdPhasesCountEndpoint import ProjectProjectsIdPhasesCountEndpoint
from pywise.models.ProjectPhaseModel import ProjectPhaseModel

class ProjectProjectsIdPhasesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "phases", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectProjectsIdPhasesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectProjectsIdPhasesIdEndpoint:
        child = ProjectProjectsIdPhasesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectPhaseModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectPhaseModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProjectPhaseModel]:
        return self._parse_many(ProjectPhaseModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProjectPhaseModel:
        return self._parse_one(ProjectPhaseModel, super().make_request("POST", params=params))
        