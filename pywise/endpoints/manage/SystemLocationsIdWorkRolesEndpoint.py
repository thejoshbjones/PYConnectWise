from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemLocationsIdWorkRolesIdEndpoint import SystemLocationsIdWorkRolesIdEndpoint
from pywise.endpoints.manage.SystemLocationsIdWorkRolesCountEndpoint import SystemLocationsIdWorkRolesCountEndpoint
from pywise.models.manage.LocationWorkRoleModel import LocationWorkRoleModel

class SystemLocationsIdWorkRolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workRoles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemLocationsIdWorkRolesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemLocationsIdWorkRolesIdEndpoint:
        child = SystemLocationsIdWorkRolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[LocationWorkRoleModel]:
        """
        Performs a GET request against the /system/locations/{parentId}/workRoles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LocationWorkRoleModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            LocationWorkRoleModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LocationWorkRoleModel]:
        """
        Performs a GET request against the /system/locations/{parentId}/workRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LocationWorkRoleModel]: The parsed response data.
        """
        return self._parse_many(LocationWorkRoleModel, super().make_request("GET", params=params).json())
        