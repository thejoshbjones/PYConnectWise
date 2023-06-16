from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectBoardsIdTeamsIdEndpoint import ProjectBoardsIdTeamsIdEndpoint
from pywise.endpoints.ProjectBoardsIdTeamsCountEndpoint import ProjectBoardsIdTeamsCountEndpoint
from pywise.endpoints.ProjectBoardsIdTeamsInfoEndpoint import ProjectBoardsIdTeamsInfoEndpoint
from pywise.models.ProjectBoardTeamModel import ProjectBoardTeamModel

class ProjectBoardsIdTeamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teams", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectBoardsIdTeamsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProjectBoardsIdTeamsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectBoardsIdTeamsIdEndpoint:
        child = ProjectBoardsIdTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectBoardTeamModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectBoardTeamModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProjectBoardTeamModel]:
        return self._parse_many(ProjectBoardTeamModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProjectBoardTeamModel:
        return self._parse_one(ProjectBoardTeamModel, super().make_request("POST", params=params))
        