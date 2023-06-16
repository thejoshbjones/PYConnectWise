from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceInfoCurrencyCodesIdEndpoint import FinanceInfoCurrencyCodesIdEndpoint
from pywise.endpoints.FinanceInfoCurrencyCodesCountEndpoint import FinanceInfoCurrencyCodesCountEndpoint
from pywise.models.CurrencyCodeModel import CurrencyCodeModel

class FinanceInfoCurrencyCodesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "currencyCodes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceInfoCurrencyCodesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceInfoCurrencyCodesIdEndpoint:
        child = FinanceInfoCurrencyCodesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CurrencyCodeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CurrencyCodeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CurrencyCodeModel]:
        return self._parse_many(CurrencyCodeModel, super().make_request("GET", params=params))
        