from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceBillingStatusesIdEndpoint import FinanceBillingStatusesIdEndpoint
from pywise.endpoints.FinanceBillingStatusesCountEndpoint import FinanceBillingStatusesCountEndpoint
from pywise.endpoints.FinanceBillingStatusesInfoEndpoint import FinanceBillingStatusesInfoEndpoint
from pywise.models.BillingStatusModel import BillingStatusModel

class FinanceBillingStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingStatuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceBillingStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceBillingStatusesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceBillingStatusesIdEndpoint:
        child = FinanceBillingStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BillingStatusModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BillingStatusModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BillingStatusModel]:
        return self._parse_many(BillingStatusModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BillingStatusModel:
        return self._parse_one(BillingStatusModel, super().make_request("POST", params=params))
        