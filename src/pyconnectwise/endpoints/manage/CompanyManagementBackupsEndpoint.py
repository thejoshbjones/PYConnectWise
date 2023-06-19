from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyManagementBackupsIdEndpoint import CompanyManagementBackupsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementBackupsCountEndpoint import CompanyManagementBackupsCountEndpoint
from pyconnectwise.models.manage.ManagementBackupModel import ManagementBackupModel

class CompanyManagementBackupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementBackups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagementBackupsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyManagementBackupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManagementBackupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManagementBackupsIdEndpoint: The initialized CompanyManagementBackupsIdEndpoint object.
        """
        child = CompanyManagementBackupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ManagementBackupModel]:
        """
        Performs a GET request against the /company/managementBackups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagementBackupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ManagementBackupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagementBackupModel]:
        """
        Performs a GET request against the /company/managementBackups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagementBackupModel]: The parsed response data.
        """
        return self._parse_many(ManagementBackupModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagementBackupModel:
        """
        Performs a POST request against the /company/managementBackups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementBackupModel: The parsed response data.
        """
        return self._parse_one(ManagementBackupModel, super().make_request("POST", params=params).json())
        