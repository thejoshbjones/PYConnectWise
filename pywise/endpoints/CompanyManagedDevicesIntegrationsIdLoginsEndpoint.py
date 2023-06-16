from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyManagedDevicesIntegrationsIdLoginsIdEndpoint import CompanyManagedDevicesIntegrationsIdLoginsIdEndpoint
from pywise.endpoints.CompanyManagedDevicesIntegrationsIdLoginsCountEndpoint import CompanyManagedDevicesIntegrationsIdLoginsCountEndpoint
from pywise.models.ManagedDevicesIntegrationLoginModel import ManagedDevicesIntegrationLoginModel

class CompanyManagedDevicesIntegrationsIdLoginsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "logins", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdLoginsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyManagedDevicesIntegrationsIdLoginsIdEndpoint:
        child = CompanyManagedDevicesIntegrationsIdLoginsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagedDevicesIntegrationLoginModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagedDevicesIntegrationLoginModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManagedDevicesIntegrationLoginModel]:
        return self._parse_many(ManagedDevicesIntegrationLoginModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ManagedDevicesIntegrationLoginModel:
        return self._parse_one(ManagedDevicesIntegrationLoginModel, super().make_request("POST", params=params))
        