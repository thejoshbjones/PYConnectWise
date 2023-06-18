from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemMycompanyReportingServicesIdEndpoint import SystemMycompanyReportingServicesIdEndpoint
from pywise.models.manage.ReportingServiceModel import ReportingServiceModel

class SystemMycompanyReportingServicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "reportingServices", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> SystemMycompanyReportingServicesIdEndpoint:
        child = SystemMycompanyReportingServicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ReportingServiceModel]:
        """
        Performs a GET request against the /system/mycompany/reportingServices endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ReportingServiceModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ReportingServiceModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ReportingServiceModel]:
        """
        Performs a GET request against the /system/mycompany/reportingServices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ReportingServiceModel]: The parsed response data.
        """
        return self._parse_many(ReportingServiceModel, super().make_request("GET", params=params).json())
        