from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectBoardsIdTeamsIdMembersIdEndpoint import ProjectBoardsIdTeamsIdMembersIdEndpoint
from pywise.models.ProjectBoardTeamMemberModel import ProjectBoardTeamMemberModel

class ProjectBoardsIdTeamsIdMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "members", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> ProjectBoardsIdTeamsIdMembersIdEndpoint:
        child = ProjectBoardsIdTeamsIdMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectBoardTeamMemberModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectBoardTeamMemberModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProjectBoardTeamMemberModel]:
        return self._parse_many(ProjectBoardTeamMemberModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProjectBoardTeamMemberModel:
        return self._parse_one(ProjectBoardTeamMemberModel, super().make_request("POST", params=params))
        