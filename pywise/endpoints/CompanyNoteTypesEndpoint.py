from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyNoteTypesIdEndpoint import CompanyNoteTypesIdEndpoint
from pywise.endpoints.CompanyNoteTypesCountEndpoint import CompanyNoteTypesCountEndpoint
from pywise.endpoints.CompanyNoteTypesInfoEndpoint import CompanyNoteTypesInfoEndpoint
from pywise.models.CompanyNoteTypeModel import CompanyNoteTypeModel

class CompanyNoteTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "noteTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyNoteTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyNoteTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyNoteTypesIdEndpoint:
        child = CompanyNoteTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyNoteTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyNoteTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanyNoteTypeModel]:
        return self._parse_many(CompanyNoteTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CompanyNoteTypeModel:
        return self._parse_one(CompanyNoteTypeModel, super().make_request("POST", params=params))
        