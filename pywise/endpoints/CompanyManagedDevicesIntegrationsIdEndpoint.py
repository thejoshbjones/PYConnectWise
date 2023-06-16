from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyManagedDevicesIntegrationsIdInfoEndpoint import CompanyManagedDevicesIntegrationsIdInfoEndpoint
from pywise.endpoints.CompanyManagedDevicesIntegrationsIdUsagesEndpoint import CompanyManagedDevicesIntegrationsIdUsagesEndpoint
from pywise.endpoints.CompanyManagedDevicesIntegrationsIdCrossReferencesEndpoint import CompanyManagedDevicesIntegrationsIdCrossReferencesEndpoint
from pywise.endpoints.CompanyManagedDevicesIntegrationsIdLoginsEndpoint import CompanyManagedDevicesIntegrationsIdLoginsEndpoint
from pywise.endpoints.CompanyManagedDevicesIntegrationsIdNotificationsEndpoint import CompanyManagedDevicesIntegrationsIdNotificationsEndpoint
from pywise.models.ManagedDevicesIntegrationModel import ManagedDevicesIntegrationModel

class CompanyManagedDevicesIntegrationsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.info = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.crossReferences = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdCrossReferencesEndpoint(client, parent_endpoint=self)
        )
        self.logins = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdLoginsEndpoint(client, parent_endpoint=self)
        )
        self.notifications = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdNotificationsEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagedDevicesIntegrationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagedDevicesIntegrationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> ManagedDevicesIntegrationModel:
        return self._parse_one(ManagedDevicesIntegrationModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> ManagedDevicesIntegrationModel:
        return self._parse_one(ManagedDevicesIntegrationModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> ManagedDevicesIntegrationModel:
        return self._parse_one(ManagedDevicesIntegrationModel, super().make_request("PATCH", params=params))
        