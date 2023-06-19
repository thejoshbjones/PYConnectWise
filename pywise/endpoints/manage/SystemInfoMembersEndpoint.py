from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemInfoMembersIdEndpoint import SystemInfoMembersIdEndpoint
from pywise.endpoints.manage.SystemInfoMembersIdEndpoint import SystemInfoMembersIdEndpoint
from pywise.endpoints.manage.SystemInfoMembersCountEndpoint import SystemInfoMembersCountEndpoint
from pywise.models.manage.MemberInfoModel import MemberInfoModel

class SystemInfoMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "members", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoMembersCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemInfoMembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoMembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoMembersIdEndpoint: The initialized SystemInfoMembersIdEndpoint object.
        """
        child = SystemInfoMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberInfoModel]:
        """
        Performs a GET request against the /system/info/members endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MemberInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberInfoModel]:
        """
        Performs a GET request against the /system/info/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberInfoModel]: The parsed response data.
        """
        return self._parse_many(MemberInfoModel, super().make_request("GET", params=params).json())
        