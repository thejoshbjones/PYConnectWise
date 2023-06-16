from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMembersIdNotificationSettingsIdEndpoint import SystemMembersIdNotificationSettingsIdEndpoint
from pywise.endpoints.SystemMembersIdNotificationSettingsCountEndpoint import SystemMembersIdNotificationSettingsCountEndpoint
from pywise.models.MemberNotificationSettingModel import MemberNotificationSettingModel

class SystemMembersIdNotificationSettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notificationSettings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersIdNotificationSettingsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMembersIdNotificationSettingsIdEndpoint:
        child = SystemMembersIdNotificationSettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MemberNotificationSettingModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MemberNotificationSettingModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MemberNotificationSettingModel]:
        return self._parse_many(MemberNotificationSettingModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MemberNotificationSettingModel:
        return self._parse_one(MemberNotificationSettingModel, super().make_request("POST", params=params))
        