from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesIdSitesIdEndpoint import CompanyCompaniesIdSitesIdEndpoint
from pywise.endpoints.CompanyCompaniesIdSitesCountEndpoint import CompanyCompaniesIdSitesCountEndpoint
from pywise.models.CompanySiteModel import CompanySiteModel

class CompanyCompaniesIdSitesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "sites", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdSitesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesIdSitesIdEndpoint:
        child = CompanyCompaniesIdSitesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanySiteModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanySiteModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanySiteModel]:
        return self._parse_many(CompanySiteModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CompanySiteModel:
        return self._parse_one(CompanySiteModel, super().make_request("POST", params=params))
        