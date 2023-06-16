from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.PaymentTypeInfoModel import PaymentTypeInfoModel

class ExpensePaymentTypesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PaymentTypeInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PaymentTypeInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PaymentTypeInfoModel]:
        return self._parse_many(PaymentTypeInfoModel, super().make_request("GET", params=params))
        