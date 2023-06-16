from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAccountingBatchesIdEntriesIdEndpoint import FinanceAccountingBatchesIdEntriesIdEndpoint
from pywise.endpoints.FinanceAccountingBatchesIdEntriesCountEndpoint import FinanceAccountingBatchesIdEntriesCountEndpoint
from pywise.models.BatchEntryModel import BatchEntryModel

class FinanceAccountingBatchesIdEntriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "entries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingBatchesIdEntriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAccountingBatchesIdEntriesIdEndpoint:
        child = FinanceAccountingBatchesIdEntriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BatchEntryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BatchEntryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BatchEntryModel]:
        return self._parse_many(BatchEntryModel, super().make_request("GET", params=params))
        