from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectSecurityRolesIdEndpoint import ProjectSecurityRolesIdEndpoint
from pywise.endpoints.ProjectSecurityRolesCountEndpoint import ProjectSecurityRolesCountEndpoint
from pywise.models.ProjectSecurityRoleModel import ProjectSecurityRoleModel

class ProjectSecurityRolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "securityRoles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectSecurityRolesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectSecurityRolesIdEndpoint:
        child = ProjectSecurityRolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectSecurityRoleModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectSecurityRoleModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProjectSecurityRoleModel]:
        return self._parse_many(ProjectSecurityRoleModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProjectSecurityRoleModel:
        return self._parse_one(ProjectSecurityRoleModel, super().make_request("POST", params=params))
        