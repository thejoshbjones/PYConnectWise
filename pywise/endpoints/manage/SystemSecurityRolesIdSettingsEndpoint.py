from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemSecurityRolesIdSettingsIdEndpoint import SystemSecurityRolesIdSettingsIdEndpoint
from pywise.endpoints.manage.SystemSecurityRolesIdSettingsCountEndpoint import SystemSecurityRolesIdSettingsCountEndpoint
from pywise.models.manage.SecurityRoleSettingModel import SecurityRoleSettingModel

class SystemSecurityRolesIdSettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "settings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemSecurityRolesIdSettingsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemSecurityRolesIdSettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSecurityRolesIdSettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSecurityRolesIdSettingsIdEndpoint: The initialized SystemSecurityRolesIdSettingsIdEndpoint object.
        """
        child = SystemSecurityRolesIdSettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SecurityRoleSettingModel]:
        """
        Performs a GET request against the /system/securityRoles/{parentId}/settings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SecurityRoleSettingModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SecurityRoleSettingModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SecurityRoleSettingModel]:
        """
        Performs a GET request against the /system/securityRoles/{parentId}/settings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SecurityRoleSettingModel]: The parsed response data.
        """
        return self._parse_many(SecurityRoleSettingModel, super().make_request("GET", params=params).json())
        