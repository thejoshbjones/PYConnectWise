from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectTicketsIdNotesIdEndpoint import ProjectTicketsIdNotesIdEndpoint
from pywise.endpoints.ProjectTicketsIdNotesCountEndpoint import ProjectTicketsIdNotesCountEndpoint
from pywise.models.TicketNoteModel import TicketNoteModel

class ProjectTicketsIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectTicketsIdNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectTicketsIdNotesIdEndpoint:
        child = ProjectTicketsIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TicketNoteModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TicketNoteModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TicketNoteModel]:
        return self._parse_many(TicketNoteModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TicketNoteModel:
        return self._parse_one(TicketNoteModel, super().make_request("POST", params=params))
        