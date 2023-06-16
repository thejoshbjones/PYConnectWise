from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyManagedDevicesIntegrationsIdEndpoint import CompanyManagedDevicesIntegrationsIdEndpoint
from pywise.endpoints.CompanyManagedDevicesIntegrationsCountEndpoint import CompanyManagedDevicesIntegrationsCountEndpoint
from pywise.endpoints.CompanyManagedDevicesIntegrationsInfoEndpoint import CompanyManagedDevicesIntegrationsInfoEndpoint
from pywise.models.ManagedDevicesIntegrationModel import ManagedDevicesIntegrationModel

class CompanyManagedDevicesIntegrationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managedDevicesIntegrations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyManagedDevicesIntegrationsIdEndpoint:
        child = CompanyManagedDevicesIntegrationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
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
    
    def get(self, data=None, params=None) -> list[ManagedDevicesIntegrationModel]:
        return self._parse_many(ManagedDevicesIntegrationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ManagedDevicesIntegrationModel:
        return self._parse_one(ManagedDevicesIntegrationModel, super().make_request("POST", params=params))
        