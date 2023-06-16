from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAccountingBatchesIdExportEndpoint import FinanceAccountingBatchesIdExportEndpoint
from pywise.endpoints.FinanceAccountingBatchesIdEntriesEndpoint import FinanceAccountingBatchesIdEntriesEndpoint
from pywise.models.AccountingBatchModel import AccountingBatchModel

class FinanceAccountingBatchesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.export = self.register_child_endpoint(
            FinanceAccountingBatchesIdExportEndpoint(client, parent_endpoint=self)
        )
        self.entries = self.register_child_endpoint(
            FinanceAccountingBatchesIdEntriesEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AccountingBatchModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AccountingBatchModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> AccountingBatchModel:
        return self._parse_one(AccountingBatchModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        