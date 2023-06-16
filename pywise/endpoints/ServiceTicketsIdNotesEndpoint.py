from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceTicketsIdNotesIdEndpoint import ServiceTicketsIdNotesIdEndpoint
from pywise.endpoints.ServiceTicketsIdNotesCountEndpoint import ServiceTicketsIdNotesCountEndpoint
from pywise.models.ServiceNoteModel import ServiceNoteModel

class ServiceTicketsIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTicketsIdNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceTicketsIdNotesIdEndpoint:
        child = ServiceTicketsIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ServiceNoteModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ServiceNoteModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ServiceNoteModel]:
        return self._parse_many(ServiceNoteModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ServiceNoteModel:
        return self._parse_one(ServiceNoteModel, super().make_request("POST", params=params))
        