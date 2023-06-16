from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesInfoTypesIdEndpoint import CompanyCompaniesInfoTypesIdEndpoint
from pywise.endpoints.CompanyCompaniesInfoTypesCountEndpoint import CompanyCompaniesInfoTypesCountEndpoint
from pywise.models.CompanyTypeInfoModel import CompanyTypeInfoModel

class CompanyCompaniesInfoTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesInfoTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesInfoTypesIdEndpoint:
        child = CompanyCompaniesInfoTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyTypeInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyTypeInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanyTypeInfoModel]:
        return self._parse_many(CompanyTypeInfoModel, super().make_request("GET", params=params))
        