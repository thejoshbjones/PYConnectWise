from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemInfoStandardNotesIdEndpoint import SystemInfoStandardNotesIdEndpoint
from pywise.endpoints.SystemInfoStandardNotesCountEndpoint import SystemInfoStandardNotesCountEndpoint
from pywise.models.StandardNoteInfoModel import StandardNoteInfoModel

class SystemInfoStandardNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "standardNotes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoStandardNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemInfoStandardNotesIdEndpoint:
        child = SystemInfoStandardNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[StandardNoteInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            StandardNoteInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[StandardNoteInfoModel]:
        return self._parse_many(StandardNoteInfoModel, super().make_request("GET", params=params))
        