from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ExpenseEntriesIdEndpoint import ExpenseEntriesIdEndpoint
from pywise.endpoints.ExpenseEntriesCountEndpoint import ExpenseEntriesCountEndpoint
from pywise.models.ExpenseEntryModel import ExpenseEntryModel

class ExpenseEntriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "entries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ExpenseEntriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ExpenseEntriesIdEndpoint:
        child = ExpenseEntriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ExpenseEntryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ExpenseEntryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ExpenseEntryModel]:
        return self._parse_many(ExpenseEntryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ExpenseEntryModel:
        return self._parse_one(ExpenseEntryModel, super().make_request("POST", params=params))
        