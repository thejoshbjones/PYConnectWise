from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesTypesIdEndpoint import CompanyCompaniesTypesIdEndpoint
from pywise.endpoints.CompanyCompaniesTypesCountEndpoint import CompanyCompaniesTypesCountEndpoint
from pywise.models.CompanyTypeModel import CompanyTypeModel

class CompanyCompaniesTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesTypesIdEndpoint:
        child = CompanyCompaniesTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanyTypeModel]:
        return self._parse_many(CompanyTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CompanyTypeModel:
        return self._parse_one(CompanyTypeModel, super().make_request("POST", params=params))
        