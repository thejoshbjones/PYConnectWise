from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMembersIdDeactivateEndpoint import SystemMembersIdDeactivateEndpoint
from pywise.endpoints.SystemMembersIdImageEndpoint import SystemMembersIdImageEndpoint
from pywise.endpoints.SystemMembersIdLinkSsoUserEndpoint import SystemMembersIdLinkSsoUserEndpoint
from pywise.endpoints.SystemMembersIdSubmitEndpoint import SystemMembersIdSubmitEndpoint
from pywise.endpoints.SystemMembersIdUnlinkSsoUserEndpoint import SystemMembersIdUnlinkSsoUserEndpoint
from pywise.endpoints.SystemMembersIdUnusedTimeSheetsEndpoint import SystemMembersIdUnusedTimeSheetsEndpoint
from pywise.endpoints.SystemMembersIdUsagesEndpoint import SystemMembersIdUsagesEndpoint
from pywise.endpoints.SystemMembersIdAccrualsEndpoint import SystemMembersIdAccrualsEndpoint
from pywise.endpoints.SystemMembersIdCertificationsEndpoint import SystemMembersIdCertificationsEndpoint
from pywise.endpoints.SystemMembersIdDelegationsEndpoint import SystemMembersIdDelegationsEndpoint
from pywise.endpoints.SystemMembersIdManagedDeviceAccountsEndpoint import SystemMembersIdManagedDeviceAccountsEndpoint
from pywise.endpoints.SystemMembersIdMycertificationsEndpoint import SystemMembersIdMycertificationsEndpoint
from pywise.endpoints.SystemMembersIdNotificationSettingsEndpoint import SystemMembersIdNotificationSettingsEndpoint
from pywise.endpoints.SystemMembersIdPersonasEndpoint import SystemMembersIdPersonasEndpoint
from pywise.endpoints.SystemMembersIdSkillsEndpoint import SystemMembersIdSkillsEndpoint
from pywise.models.MemberModel import MemberModel

class SystemMembersIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
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
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MemberModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MemberModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> MemberModel:
        return self._parse_one(MemberModel, super().make_request("GET", params=params))
        
    def put(self, data=None, params=None) -> MemberModel:
        return self._parse_one(MemberModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> MemberModel:
        return self._parse_one(MemberModel, super().make_request("PATCH", params=params))
        