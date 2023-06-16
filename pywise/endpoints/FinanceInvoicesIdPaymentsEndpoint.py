from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceInvoicesIdPaymentsIdEndpoint import FinanceInvoicesIdPaymentsIdEndpoint
from pywise.models.PaymentModel import PaymentModel

class FinanceInvoicesIdPaymentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "payments", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> FinanceInvoicesIdPaymentsIdEndpoint:
        child = FinanceInvoicesIdPaymentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PaymentModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PaymentModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PaymentModel]:
        return self._parse_many(PaymentModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> PaymentModel:
        return self._parse_one(PaymentModel, super().make_request("POST", params=params))
        