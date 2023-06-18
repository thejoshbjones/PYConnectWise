from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemMembersIdAccrualsIdEndpoint import SystemMembersIdAccrualsIdEndpoint
from pywise.endpoints.manage.SystemMembersIdAccrualsCountEndpoint import SystemMembersIdAccrualsCountEndpoint
from pywise.models.manage.MemberAccrualModel import MemberAccrualModel

class SystemMembersIdAccrualsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "accruals", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersIdAccrualsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMembersIdAccrualsIdEndpoint:
        child = SystemMembersIdAccrualsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberAccrualModel]:
        """
        Performs a GET request against the /system/members/{parentId}/accruals endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberAccrualModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MemberAccrualModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberAccrualModel]:
        """
        Performs a GET request against the /system/members/{parentId}/accruals endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberAccrualModel]: The parsed response data.
        """
        return self._parse_many(MemberAccrualModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberAccrualModel:
        """
        Performs a POST request against the /system/members/{parentId}/accruals endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberAccrualModel: The parsed response data.
        """
        return self._parse_one(MemberAccrualModel, super().make_request("POST", params=params).json())
        