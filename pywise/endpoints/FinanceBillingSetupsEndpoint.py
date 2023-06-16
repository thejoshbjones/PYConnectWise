from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceBillingSetupsIdEndpoint import FinanceBillingSetupsIdEndpoint
from pywise.endpoints.FinanceBillingSetupsCountEndpoint import FinanceBillingSetupsCountEndpoint
from pywise.endpoints.FinanceBillingSetupsInfoEndpoint import FinanceBillingSetupsInfoEndpoint
from pywise.models.BillingSetupModel import BillingSetupModel

class FinanceBillingSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceBillingSetupsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceBillingSetupsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceBillingSetupsIdEndpoint:
        child = FinanceBillingSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BillingSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BillingSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BillingSetupModel]:
        return self._parse_many(BillingSetupModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BillingSetupModel:
        return self._parse_one(BillingSetupModel, super().make_request("POST", params=params))
        