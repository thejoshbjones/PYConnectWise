from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectProjectsIdEndpoint import ProjectProjectsIdEndpoint
from pywise.endpoints.ProjectProjectsCountEndpoint import ProjectProjectsCountEndpoint
from pywise.models.ProjectModel import ProjectModel

class ProjectProjectsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "projects", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectProjectsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectProjectsIdEndpoint:
        child = ProjectProjectsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProjectModel]:
        return self._parse_many(ProjectModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProjectModel:
        return self._parse_one(ProjectModel, super().make_request("POST", params=params))
        