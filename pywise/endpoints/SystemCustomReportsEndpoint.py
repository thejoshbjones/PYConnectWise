from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemCustomReportsIdEndpoint import SystemCustomReportsIdEndpoint
from pywise.endpoints.SystemCustomReportsCountEndpoint import SystemCustomReportsCountEndpoint
from pywise.models.CustomReportModel import CustomReportModel

class SystemCustomReportsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "customReports", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemCustomReportsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemCustomReportsIdEndpoint:
        child = SystemCustomReportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CustomReportModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CustomReportModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CustomReportModel]:
        return self._parse_many(CustomReportModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CustomReportModel:
        return self._parse_one(CustomReportModel, super().make_request("POST", params=params))
        