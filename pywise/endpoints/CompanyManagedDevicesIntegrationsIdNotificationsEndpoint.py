from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyManagedDevicesIntegrationsIdNotificationsIdEndpoint import CompanyManagedDevicesIntegrationsIdNotificationsIdEndpoint
from pywise.endpoints.CompanyManagedDevicesIntegrationsIdNotificationsCountEndpoint import CompanyManagedDevicesIntegrationsIdNotificationsCountEndpoint
from pywise.models.ManagedDevicesIntegrationNotificationModel import ManagedDevicesIntegrationNotificationModel

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
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagedDevicesIntegrationNotificationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagedDevicesIntegrationNotificationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManagedDevicesIntegrationNotificationModel]:
        return self._parse_many(ManagedDevicesIntegrationNotificationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ManagedDevicesIntegrationNotificationModel:
        return self._parse_one(ManagedDevicesIntegrationNotificationModel, super().make_request("POST", params=params))
        