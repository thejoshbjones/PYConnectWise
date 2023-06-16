from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyManagedDevicesIntegrationsInfoCountEndpoint import CompanyManagedDevicesIntegrationsInfoCountEndpoint
from pywise.models.ManagedDevicesIntegrationInfoModel import ManagedDevicesIntegrationInfoModel

class CompanyManagedDevicesIntegrationsInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagedDevicesIntegrationInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagedDevicesIntegrationInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManagedDevicesIntegrationInfoModel]:
        return self._parse_many(ManagedDevicesIntegrationInfoModel, super().make_request("GET", params=params))
        