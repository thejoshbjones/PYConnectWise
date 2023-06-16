from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemCustomReportsIdParametersIdEndpoint import SystemCustomReportsIdParametersIdEndpoint
from pywise.endpoints.SystemCustomReportsIdParametersCountEndpoint import SystemCustomReportsIdParametersCountEndpoint
from pywise.models.CustomReportParameterModel import CustomReportParameterModel

class SystemCustomReportsIdParametersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parameters", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemCustomReportsIdParametersCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemCustomReportsIdParametersIdEndpoint:
        child = SystemCustomReportsIdParametersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CustomReportParameterModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CustomReportParameterModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CustomReportParameterModel]:
        return self._parse_many(CustomReportParameterModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CustomReportParameterModel:
        return self._parse_one(CustomReportParameterModel, super().make_request("POST", params=params))
        