from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceBillingCyclesIdEndpoint import FinanceBillingCyclesIdEndpoint
from pywise.endpoints.FinanceBillingCyclesCountEndpoint import FinanceBillingCyclesCountEndpoint
from pywise.endpoints.FinanceBillingCyclesInfoEndpoint import FinanceBillingCyclesInfoEndpoint
from pywise.models.BillingCycleModel import BillingCycleModel

class FinanceBillingCyclesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingCycles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceBillingCyclesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceBillingCyclesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceBillingCyclesIdEndpoint:
        child = FinanceBillingCyclesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BillingCycleModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BillingCycleModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BillingCycleModel]:
        return self._parse_many(BillingCycleModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BillingCycleModel:
        return self._parse_one(BillingCycleModel, super().make_request("POST", params=params))
        