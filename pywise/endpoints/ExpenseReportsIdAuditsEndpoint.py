from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ExpenseReportsIdAuditsIdEndpoint import ExpenseReportsIdAuditsIdEndpoint
from pywise.endpoints.ExpenseReportsIdAuditsCountEndpoint import ExpenseReportsIdAuditsCountEndpoint
from pywise.models.ExpenseReportAuditModel import ExpenseReportAuditModel

class ExpenseReportsIdAuditsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "audits", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ExpenseReportsIdAuditsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ExpenseReportsIdAuditsIdEndpoint:
        child = ExpenseReportsIdAuditsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ExpenseReportAuditModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ExpenseReportAuditModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ExpenseReportAuditModel]:
        return self._parse_many(ExpenseReportAuditModel, super().make_request("GET", params=params))
        