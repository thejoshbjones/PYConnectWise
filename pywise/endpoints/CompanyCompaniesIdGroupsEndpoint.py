from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesIdGroupsIdEndpoint import CompanyCompaniesIdGroupsIdEndpoint
from pywise.endpoints.CompanyCompaniesIdGroupsCountEndpoint import CompanyCompaniesIdGroupsCountEndpoint
from pywise.models.CompanyGroupModel import CompanyGroupModel

class CompanyCompaniesIdGroupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "groups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdGroupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesIdGroupsIdEndpoint:
        child = CompanyCompaniesIdGroupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyGroupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyGroupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanyGroupModel]:
        return self._parse_many(CompanyGroupModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CompanyGroupModel:
        return self._parse_one(CompanyGroupModel, super().make_request("POST", params=params))
        