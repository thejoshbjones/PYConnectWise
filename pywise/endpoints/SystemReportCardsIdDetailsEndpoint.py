from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemReportCardsIdDetailsIdEndpoint import SystemReportCardsIdDetailsIdEndpoint
from pywise.endpoints.SystemReportCardsIdDetailsCountEndpoint import SystemReportCardsIdDetailsCountEndpoint
from pywise.models.ReportCardDetailModel import ReportCardDetailModel

class SystemReportCardsIdDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "details", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemReportCardsIdDetailsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemReportCardsIdDetailsIdEndpoint:
        child = SystemReportCardsIdDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ReportCardDetailModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ReportCardDetailModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ReportCardDetailModel]:
        return self._parse_many(ReportCardDetailModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ReportCardDetailModel:
        return self._parse_one(ReportCardDetailModel, super().make_request("POST", params=params))
        