from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceTaxIntegrationsIdEndpoint import FinanceTaxIntegrationsIdEndpoint
from pywise.endpoints.FinanceTaxIntegrationsCountEndpoint import FinanceTaxIntegrationsCountEndpoint
from pywise.models.TaxIntegrationModel import TaxIntegrationModel

class FinanceTaxIntegrationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxIntegrations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxIntegrationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceTaxIntegrationsIdEndpoint:
        child = FinanceTaxIntegrationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TaxIntegrationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TaxIntegrationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TaxIntegrationModel]:
        return self._parse_many(TaxIntegrationModel, super().make_request("GET", params=params))
        