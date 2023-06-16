from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemStandardNotesIdEndpoint import SystemStandardNotesIdEndpoint
from pywise.endpoints.SystemStandardNotesCountEndpoint import SystemStandardNotesCountEndpoint
from pywise.models.StandardNoteModel import StandardNoteModel

class SystemStandardNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "standardNotes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemStandardNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemStandardNotesIdEndpoint:
        child = SystemStandardNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[StandardNoteModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            StandardNoteModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[StandardNoteModel]:
        return self._parse_many(StandardNoteModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> StandardNoteModel:
        return self._parse_one(StandardNoteModel, super().make_request("POST", params=params))
        