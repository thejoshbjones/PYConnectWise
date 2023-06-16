from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemPortalReportsIdEndpoint import SystemPortalReportsIdEndpoint
from pywise.endpoints.SystemPortalReportsCountEndpoint import SystemPortalReportsCountEndpoint
from pywise.models.PortalReportModel import PortalReportModel

class SystemPortalReportsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "portalReports", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemPortalReportsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemPortalReportsIdEndpoint:
        child = SystemPortalReportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PortalReportModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PortalReportModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PortalReportModel]:
        return self._parse_many(PortalReportModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> PortalReportModel:
        return self._parse_one(PortalReportModel, super().make_request("POST", params=params))
        