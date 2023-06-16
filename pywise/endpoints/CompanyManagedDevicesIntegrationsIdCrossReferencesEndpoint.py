from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyManagedDevicesIntegrationsIdCrossReferencesIdEndpoint import CompanyManagedDevicesIntegrationsIdCrossReferencesIdEndpoint
from pywise.endpoints.CompanyManagedDevicesIntegrationsIdCrossReferencesCountEndpoint import CompanyManagedDevicesIntegrationsIdCrossReferencesCountEndpoint
from pywise.models.ManagedDevicesIntegrationCrossReferenceModel import ManagedDevicesIntegrationCrossReferenceModel

class CompanyManagedDevicesIntegrationsIdCrossReferencesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "crossReferences", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagedDevicesIntegrationsIdCrossReferencesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyManagedDevicesIntegrationsIdCrossReferencesIdEndpoint:
        child = CompanyManagedDevicesIntegrationsIdCrossReferencesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagedDevicesIntegrationCrossReferenceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagedDevicesIntegrationCrossReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManagedDevicesIntegrationCrossReferenceModel]:
        return self._parse_many(ManagedDevicesIntegrationCrossReferenceModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ManagedDevicesIntegrationCrossReferenceModel:
        return self._parse_one(ManagedDevicesIntegrationCrossReferenceModel, super().make_request("POST", params=params))
        