from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesIdCustomStatusNotesIdEndpoint import CompanyCompaniesIdCustomStatusNotesIdEndpoint
from pywise.endpoints.CompanyCompaniesIdCustomStatusNotesCountEndpoint import CompanyCompaniesIdCustomStatusNotesCountEndpoint
from pywise.models.CompanyCustomNoteModel import CompanyCustomNoteModel

class CompanyCompaniesIdCustomStatusNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "customStatusNotes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdCustomStatusNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesIdCustomStatusNotesIdEndpoint:
        child = CompanyCompaniesIdCustomStatusNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyCustomNoteModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyCustomNoteModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanyCustomNoteModel]:
        return self._parse_many(CompanyCustomNoteModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CompanyCustomNoteModel:
        return self._parse_one(CompanyCustomNoteModel, super().make_request("POST", params=params))
        