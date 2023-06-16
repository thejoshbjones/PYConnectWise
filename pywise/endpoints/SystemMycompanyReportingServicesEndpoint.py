from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMycompanyReportingServicesIdEndpoint import SystemMycompanyReportingServicesIdEndpoint
from pywise.models.ReportingServiceModel import ReportingServiceModel

class SystemMycompanyReportingServicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "reportingServices", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> SystemMycompanyReportingServicesIdEndpoint:
        child = SystemMycompanyReportingServicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ReportingServiceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ReportingServiceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ReportingServiceModel]:
        return self._parse_many(ReportingServiceModel, super().make_request("GET", params=params))
        