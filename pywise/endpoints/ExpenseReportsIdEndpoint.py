from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ExpenseReportsIdReverseEndpoint import ExpenseReportsIdReverseEndpoint
from pywise.endpoints.ExpenseReportsIdSubmitEndpoint import ExpenseReportsIdSubmitEndpoint
from pywise.endpoints.ExpenseReportsIdAuditsEndpoint import ExpenseReportsIdAuditsEndpoint
from pywise.models.ExpenseReportModel import ExpenseReportModel

class ExpenseReportsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.reverse = self.register_child_endpoint(
            ExpenseReportsIdReverseEndpoint(client, parent_endpoint=self)
        )
        self.submit = self.register_child_endpoint(
            ExpenseReportsIdSubmitEndpoint(client, parent_endpoint=self)
        )
        self.audits = self.register_child_endpoint(
            ExpenseReportsIdAuditsEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ExpenseReportModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ExpenseReportModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> ExpenseReportModel:
        return self._parse_one(ExpenseReportModel, super().make_request("GET", params=params))
        