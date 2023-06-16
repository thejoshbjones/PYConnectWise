from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectProjectsIdContactsEndpoint import ProjectProjectsIdContactsEndpoint
from pywise.endpoints.ProjectProjectsIdNotesEndpoint import ProjectProjectsIdNotesEndpoint
from pywise.endpoints.ProjectProjectsIdPhasesEndpoint import ProjectProjectsIdPhasesEndpoint
from pywise.endpoints.ProjectProjectsIdTeamMembersEndpoint import ProjectProjectsIdTeamMembersEndpoint
from pywise.models.ProjectModel import ProjectModel

class ProjectProjectsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.contacts = self.register_child_endpoint(
            ProjectProjectsIdContactsEndpoint(client, parent_endpoint=self)
        )
        self.notes = self.register_child_endpoint(
            ProjectProjectsIdNotesEndpoint(client, parent_endpoint=self)
        )
        self.phases = self.register_child_endpoint(
            ProjectProjectsIdPhasesEndpoint(client, parent_endpoint=self)
        )
        self.teamMembers = self.register_child_endpoint(
            ProjectProjectsIdTeamMembersEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> ProjectModel:
        return self._parse_one(ProjectModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> ProjectModel:
        return self._parse_one(ProjectModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> ProjectModel:
        return self._parse_one(ProjectModel, super().make_request("PATCH", params=params))
        