from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemReportCardsIdEndpoint import SystemReportCardsIdEndpoint
from pywise.endpoints.SystemReportCardsCountEndpoint import SystemReportCardsCountEndpoint
from pywise.endpoints.SystemReportCardsInfoEndpoint import SystemReportCardsInfoEndpoint
from pywise.models.ReportCardModel import ReportCardModel

class SystemReportCardsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "reportCards", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemReportCardsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemReportCardsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemReportCardsIdEndpoint:
        child = SystemReportCardsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ReportCardModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ReportCardModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ReportCardModel]:
        return self._parse_many(ReportCardModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ReportCardModel:
        return self._parse_one(ReportCardModel, super().make_request("POST", params=params))
        