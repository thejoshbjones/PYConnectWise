from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ExpenseInfoTaxTypesIdEndpoint import ExpenseInfoTaxTypesIdEndpoint
from pywise.endpoints.ExpenseInfoTaxTypesCountEndpoint import ExpenseInfoTaxTypesCountEndpoint
from pywise.models.ExpenseTaxTypeInfoModel import ExpenseTaxTypeInfoModel

class ExpenseInfoTaxTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ExpenseInfoTaxTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ExpenseInfoTaxTypesIdEndpoint:
        child = ExpenseInfoTaxTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ExpenseTaxTypeInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ExpenseTaxTypeInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ExpenseTaxTypeInfoModel]:
        return self._parse_many(ExpenseTaxTypeInfoModel, super().make_request("GET", params=params))
        