from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectProjectsIdNotesIdEndpoint import ProjectProjectsIdNotesIdEndpoint
from pywise.endpoints.ProjectProjectsIdNotesCountEndpoint import ProjectProjectsIdNotesCountEndpoint
from pywise.models.ProjectNoteModel import ProjectNoteModel

class ProjectProjectsIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectProjectsIdNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectProjectsIdNotesIdEndpoint:
        child = ProjectProjectsIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectNoteModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectNoteModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProjectNoteModel]:
        return self._parse_many(ProjectNoteModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProjectNoteModel:
        return self._parse_one(ProjectNoteModel, super().make_request("POST", params=params))
        