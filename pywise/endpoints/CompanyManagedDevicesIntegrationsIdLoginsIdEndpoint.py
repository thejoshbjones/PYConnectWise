from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.ManagedDevicesIntegrationLoginModel import ManagedDevicesIntegrationLoginModel

class CompanyManagedDevicesIntegrationsIdLoginsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
    
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
    
    def get(self, data=None, params=None) -> ManagedDevicesIntegrationLoginModel:
        return self._parse_one(ManagedDevicesIntegrationLoginModel, super().make_request("GET", params=params))
        
    def put(self, data=None, params=None) -> ManagedDevicesIntegrationLoginModel:
        return self._parse_one(ManagedDevicesIntegrationLoginModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> ManagedDevicesIntegrationLoginModel:
        return self._parse_one(ManagedDevicesIntegrationLoginModel, super().make_request("PATCH", params=params))
        
    def delete(self, data=None, params=None) -> ManagedDevicesIntegrationLoginModel:
        return self._parse_one(ManagedDevicesIntegrationLoginModel, super().make_request("DELETE", params=params))
        