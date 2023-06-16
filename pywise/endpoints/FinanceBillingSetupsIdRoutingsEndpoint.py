from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceBillingSetupsIdRoutingsIdEndpoint import FinanceBillingSetupsIdRoutingsIdEndpoint
from pywise.endpoints.FinanceBillingSetupsIdRoutingsCountEndpoint import FinanceBillingSetupsIdRoutingsCountEndpoint
from pywise.models.BillingSetupRoutingModel import BillingSetupRoutingModel

class FinanceBillingSetupsIdRoutingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "routings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceBillingSetupsIdRoutingsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceBillingSetupsIdRoutingsIdEndpoint:
        child = FinanceBillingSetupsIdRoutingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BillingSetupRoutingModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BillingSetupRoutingModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BillingSetupRoutingModel]:
        return self._parse_many(BillingSetupRoutingModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BillingSetupRoutingModel:
        return self._parse_one(BillingSetupRoutingModel, super().make_request("POST", params=params))
        