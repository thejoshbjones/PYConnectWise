from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemMembersIdPersonasIdEndpoint import SystemMembersIdPersonasIdEndpoint
from pywise.endpoints.manage.SystemMembersIdPersonasCountEndpoint import SystemMembersIdPersonasCountEndpoint
from pywise.models.manage.MemberPersonaModel import MemberPersonaModel

class SystemMembersIdPersonasEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "personas", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersIdPersonasCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMembersIdPersonasIdEndpoint:
        child = SystemMembersIdPersonasIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberPersonaModel]:
        """
        Performs a GET request against the /system/members/{parentId}/personas endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberPersonaModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MemberPersonaModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberPersonaModel]:
        """
        Performs a GET request against the /system/members/{parentId}/personas endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberPersonaModel]: The parsed response data.
        """
        return self._parse_many(MemberPersonaModel, super().make_request("GET", params=params).json())
        