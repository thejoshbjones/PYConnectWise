from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemMembersIdDeactivateEndpoint import SystemMembersIdDeactivateEndpoint
from pywise.endpoints.manage.SystemMembersIdImageEndpoint import SystemMembersIdImageEndpoint
from pywise.endpoints.manage.SystemMembersIdLinkSsoUserEndpoint import SystemMembersIdLinkSsoUserEndpoint
from pywise.endpoints.manage.SystemMembersIdSubmitEndpoint import SystemMembersIdSubmitEndpoint
from pywise.endpoints.manage.SystemMembersIdUnlinkSsoUserEndpoint import SystemMembersIdUnlinkSsoUserEndpoint
from pywise.endpoints.manage.SystemMembersIdUnusedTimeSheetsEndpoint import SystemMembersIdUnusedTimeSheetsEndpoint
from pywise.endpoints.manage.SystemMembersIdUsagesEndpoint import SystemMembersIdUsagesEndpoint
from pywise.endpoints.manage.SystemMembersIdAccrualsEndpoint import SystemMembersIdAccrualsEndpoint
from pywise.endpoints.manage.SystemMembersIdCertificationsEndpoint import SystemMembersIdCertificationsEndpoint
from pywise.endpoints.manage.SystemMembersIdDelegationsEndpoint import SystemMembersIdDelegationsEndpoint
from pywise.endpoints.manage.SystemMembersIdManagedDeviceAccountsEndpoint import SystemMembersIdManagedDeviceAccountsEndpoint
from pywise.endpoints.manage.SystemMembersIdMycertificationsEndpoint import SystemMembersIdMycertificationsEndpoint
from pywise.endpoints.manage.SystemMembersIdNotificationSettingsEndpoint import SystemMembersIdNotificationSettingsEndpoint
from pywise.endpoints.manage.SystemMembersIdPersonasEndpoint import SystemMembersIdPersonasEndpoint
from pywise.endpoints.manage.SystemMembersIdSkillsEndpoint import SystemMembersIdSkillsEndpoint
from pywise.models.manage.MemberModel import MemberModel

class SystemMembersIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.deactivate = self.register_child_endpoint(
            SystemMembersIdDeactivateEndpoint(client, parent_endpoint=self)
        )
        self.image = self.register_child_endpoint(
            SystemMembersIdImageEndpoint(client, parent_endpoint=self)
        )
        self.linkSsoUser = self.register_child_endpoint(
            SystemMembersIdLinkSsoUserEndpoint(client, parent_endpoint=self)
        )
        self.submit = self.register_child_endpoint(
            SystemMembersIdSubmitEndpoint(client, parent_endpoint=self)
        )
        self.unlinkSsoUser = self.register_child_endpoint(
            SystemMembersIdUnlinkSsoUserEndpoint(client, parent_endpoint=self)
        )
        self.unusedTimeSheets = self.register_child_endpoint(
            SystemMembersIdUnusedTimeSheetsEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            SystemMembersIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.accruals = self.register_child_endpoint(
            SystemMembersIdAccrualsEndpoint(client, parent_endpoint=self)
        )
        self.certifications = self.register_child_endpoint(
            SystemMembersIdCertificationsEndpoint(client, parent_endpoint=self)
        )
        self.delegations = self.register_child_endpoint(
            SystemMembersIdDelegationsEndpoint(client, parent_endpoint=self)
        )
        self.managedDeviceAccounts = self.register_child_endpoint(
            SystemMembersIdManagedDeviceAccountsEndpoint(client, parent_endpoint=self)
        )
        self.mycertifications = self.register_child_endpoint(
            SystemMembersIdMycertificationsEndpoint(client, parent_endpoint=self)
        )
        self.notificationSettings = self.register_child_endpoint(
            SystemMembersIdNotificationSettingsEndpoint(client, parent_endpoint=self)
        )
        self.personas = self.register_child_endpoint(
            SystemMembersIdPersonasEndpoint(client, parent_endpoint=self)
        )
        self.skills = self.register_child_endpoint(
            SystemMembersIdSkillsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberModel]:
        """
        Performs a GET request against the /system/members/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MemberModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberModel:
        """
        Performs a GET request against the /system/members/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberModel: The parsed response data.
        """
        return self._parse_one(MemberModel, super().make_request("GET", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberModel:
        """
        Performs a PUT request against the /system/members/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberModel: The parsed response data.
        """
        return self._parse_one(MemberModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberModel:
        """
        Performs a PATCH request against the /system/members/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberModel: The parsed response data.
        """
        return self._parse_one(MemberModel, super().make_request("PATCH", params=params).json())
        