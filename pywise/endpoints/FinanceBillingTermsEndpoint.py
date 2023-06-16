from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceBillingTermsIdEndpoint import FinanceBillingTermsIdEndpoint
from pywise.endpoints.FinanceBillingTermsCountEndpoint import FinanceBillingTermsCountEndpoint
from pywise.endpoints.FinanceBillingTermsInfoEndpoint import FinanceBillingTermsInfoEndpoint
from pywise.models.BillingTermModel import BillingTermModel

class FinanceBillingTermsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingTerms", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceBillingTermsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceBillingTermsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceBillingTermsIdEndpoint:
        child = FinanceBillingTermsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BillingTermModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BillingTermModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BillingTermModel]:
        return self._parse_many(BillingTermModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BillingTermModel:
        return self._parse_one(BillingTermModel, super().make_request("POST", params=params))
        