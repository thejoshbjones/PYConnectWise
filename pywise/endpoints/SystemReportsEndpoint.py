from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemReportsIdEndpoint import SystemReportsIdEndpoint
from pywise.models.ReportModel import ReportModel

class SystemReportsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "reports", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> SystemReportsIdEndpoint:
        child = SystemReportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ReportModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ReportModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ReportModel]:
        return self._parse_many(ReportModel, super().make_request("GET", params=params))
        