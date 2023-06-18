from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemMembersIdNotificationSettingsIdEndpoint import SystemMembersIdNotificationSettingsIdEndpoint
from pywise.endpoints.manage.SystemMembersIdNotificationSettingsCountEndpoint import SystemMembersIdNotificationSettingsCountEndpoint
from pywise.models.manage.MemberNotificationSettingModel import MemberNotificationSettingModel

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
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberNotificationSettingModel]:
        """
        Performs a GET request against the /system/members/{parentId}/notificationSettings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberNotificationSettingModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MemberNotificationSettingModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberNotificationSettingModel]:
        """
        Performs a GET request against the /system/members/{parentId}/notificationSettings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberNotificationSettingModel]: The parsed response data.
        """
        return self._parse_many(MemberNotificationSettingModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberNotificationSettingModel:
        """
        Performs a POST request against the /system/members/{parentId}/notificationSettings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberNotificationSettingModel: The parsed response data.
        """
        return self._parse_one(MemberNotificationSettingModel, super().make_request("POST", params=params).json())
        