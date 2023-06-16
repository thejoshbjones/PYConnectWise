from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectProjectsIdTeamMembersIdEndpoint import ProjectProjectsIdTeamMembersIdEndpoint
from pywise.endpoints.ProjectProjectsIdTeamMembersCountEndpoint import ProjectProjectsIdTeamMembersCountEndpoint
from pywise.models.ProjectTeamMemberModel import ProjectTeamMemberModel

class ProjectProjectsIdTeamMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teamMembers", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectProjectsIdTeamMembersCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectProjectsIdTeamMembersIdEndpoint:
        child = ProjectProjectsIdTeamMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectTeamMemberModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectTeamMemberModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProjectTeamMemberModel]:
        return self._parse_many(ProjectTeamMemberModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProjectTeamMemberModel:
        return self._parse_one(ProjectTeamMemberModel, super().make_request("POST", params=params))
        