from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyContactsIdNotesIdEndpoint import CompanyContactsIdNotesIdEndpoint
from pywise.endpoints.CompanyContactsIdNotesCountEndpoint import CompanyContactsIdNotesCountEndpoint
from pywise.models.ContactNoteModel import ContactNoteModel

class CompanyContactsIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsIdNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyContactsIdNotesIdEndpoint:
        child = CompanyContactsIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ContactNoteModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ContactNoteModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ContactNoteModel]:
        return self._parse_many(ContactNoteModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ContactNoteModel:
        return self._parse_one(ContactNoteModel, super().make_request("POST", params=params))
        