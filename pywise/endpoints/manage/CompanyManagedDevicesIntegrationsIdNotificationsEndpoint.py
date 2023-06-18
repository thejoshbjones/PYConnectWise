from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyManagedDevicesIntegrationsIdNotificationsIdEndpoint import CompanyManagedDevicesIntegrationsIdNotificationsIdEndpoint
from pywise.endpoints.manage.CompanyManagedDevicesIntegrationsIdNotificationsCountEndpoint import CompanyManagedDevicesIntegrationsIdNotificationsCountEndpoint
from pywise.models.manage.ManagedDevicesIntegrationNotificationModel import ManagedDevicesIntegrationNotificationModel

class CompanyManagedDevicesIntegrationsIdNotificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notifications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdNotificationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyManagedDevicesIntegrationsIdNotificationsIdEndpoint:
        child = CompanyManagedDevicesIntegrationsIdNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ManagedDevicesIntegrationNotificationModel]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{parentId}/notifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDevicesIntegrationNotificationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ManagedDevicesIntegrationNotificationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagedDevicesIntegrationNotificationModel]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{parentId}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagedDevicesIntegrationNotificationModel]: The parsed response data.
        """
        return self._parse_many(ManagedDevicesIntegrationNotificationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegrationNotificationModel:
        """
        Performs a POST request against the /company/managedDevicesIntegrations/{parentId}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationNotificationModel: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegrationNotificationModel, super().make_request("POST", params=params).json())
        