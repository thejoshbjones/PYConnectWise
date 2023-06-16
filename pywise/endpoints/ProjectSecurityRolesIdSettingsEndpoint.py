from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectSecurityRolesIdSettingsIdEndpoint import ProjectSecurityRolesIdSettingsIdEndpoint
from pywise.endpoints.ProjectSecurityRolesIdSettingsCountEndpoint import ProjectSecurityRolesIdSettingsCountEndpoint
from pywise.models.ProjectSecurityRoleSettingModel import ProjectSecurityRoleSettingModel

class ProjectSecurityRolesIdSettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "settings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectSecurityRolesIdSettingsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectSecurityRolesIdSettingsIdEndpoint:
        child = ProjectSecurityRolesIdSettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectSecurityRoleSettingModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectSecurityRoleSettingModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProjectSecurityRoleSettingModel]:
        return self._parse_many(ProjectSecurityRoleSettingModel, super().make_request("GET", params=params))
        