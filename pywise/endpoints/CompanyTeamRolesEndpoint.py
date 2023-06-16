from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyTeamRolesIdEndpoint import CompanyTeamRolesIdEndpoint
from pywise.endpoints.CompanyTeamRolesCountEndpoint import CompanyTeamRolesCountEndpoint
from pywise.endpoints.CompanyTeamRolesInfoEndpoint import CompanyTeamRolesInfoEndpoint
from pywise.models.TeamRoleModel import TeamRoleModel

class CompanyTeamRolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teamRoles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyTeamRolesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyTeamRolesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyTeamRolesIdEndpoint:
        child = CompanyTeamRolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TeamRoleModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TeamRoleModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TeamRoleModel]:
        return self._parse_many(TeamRoleModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TeamRoleModel:
        return self._parse_one(TeamRoleModel, super().make_request("POST", params=params))
        