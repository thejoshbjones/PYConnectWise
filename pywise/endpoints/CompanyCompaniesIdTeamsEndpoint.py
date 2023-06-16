from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesIdTeamsIdEndpoint import CompanyCompaniesIdTeamsIdEndpoint
from pywise.endpoints.CompanyCompaniesIdTeamsCountEndpoint import CompanyCompaniesIdTeamsCountEndpoint
from pywise.models.CompanyTeamModel import CompanyTeamModel

class CompanyCompaniesIdTeamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teams", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdTeamsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesIdTeamsIdEndpoint:
        child = CompanyCompaniesIdTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyTeamModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyTeamModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanyTeamModel]:
        return self._parse_many(CompanyTeamModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CompanyTeamModel:
        return self._parse_one(CompanyTeamModel, super().make_request("POST", params=params))
        