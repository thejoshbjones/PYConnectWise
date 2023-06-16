from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemReportsIdColumnsEndpoint import SystemReportsIdColumnsEndpoint
from pywise.endpoints.SystemReportsIdCountEndpoint import SystemReportsIdCountEndpoint
from pywise.models.ReportDataResponseModel import ReportDataResponseModel

class SystemReportsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{reportName}", parent_endpoint=parent_endpoint)
        
        self.columns = self.register_child_endpoint(
            SystemReportsIdColumnsEndpoint(client, parent_endpoint=self)
        )
        self.count = self.register_child_endpoint(
            SystemReportsIdCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ReportDataResponseModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ReportDataResponseModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> ReportDataResponseModel:
        return self._parse_one(ReportDataResponseModel, super().make_request("GET", params=params))
        