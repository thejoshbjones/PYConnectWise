from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ExpenseEntriesIdAuditsIdEndpoint import ExpenseEntriesIdAuditsIdEndpoint
from pywise.endpoints.ExpenseEntriesIdAuditsCountEndpoint import ExpenseEntriesIdAuditsCountEndpoint
from pywise.models.ExpenseEntryAuditModel import ExpenseEntryAuditModel

class ExpenseEntriesIdAuditsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "audits", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ExpenseEntriesIdAuditsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ExpenseEntriesIdAuditsIdEndpoint:
        child = ExpenseEntriesIdAuditsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ExpenseEntryAuditModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ExpenseEntryAuditModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ExpenseEntryAuditModel]:
        return self._parse_many(ExpenseEntryAuditModel, super().make_request("GET", params=params))
        