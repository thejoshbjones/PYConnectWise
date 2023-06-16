from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesIdNotesIdEndpoint import CompanyCompaniesIdNotesIdEndpoint
from pywise.endpoints.CompanyCompaniesIdNotesCountEndpoint import CompanyCompaniesIdNotesCountEndpoint
from pywise.models.CompanyNoteModel import CompanyNoteModel

class CompanyCompaniesIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesIdNotesIdEndpoint:
        child = CompanyCompaniesIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyNoteModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyNoteModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanyNoteModel]:
        return self._parse_many(CompanyNoteModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CompanyNoteModel:
        return self._parse_one(CompanyNoteModel, super().make_request("POST", params=params))
        