from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesIdEndpoint import CompanyCompaniesIdEndpoint
from pywise.endpoints.CompanyCompaniesCountEndpoint import CompanyCompaniesCountEndpoint
from pywise.endpoints.CompanyCompaniesDefaultEndpoint import CompanyCompaniesDefaultEndpoint
from pywise.endpoints.CompanyCompaniesStatusesEndpoint import CompanyCompaniesStatusesEndpoint
from pywise.endpoints.CompanyCompaniesTypesEndpoint import CompanyCompaniesTypesEndpoint
from pywise.models.CompanyModel import CompanyModel

class CompanyCompaniesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "companies", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self.register_child_endpoint(
            CompanyCompaniesDefaultEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            CompanyCompaniesStatusesEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            CompanyCompaniesTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesIdEndpoint:
        child = CompanyCompaniesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanyModel]:
        return self._parse_many(CompanyModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CompanyModel:
        return self._parse_one(CompanyModel, super().make_request("POST", params=params))
        