from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemSurveysIdEndpoint import SystemSurveysIdEndpoint
from pywise.endpoints.SystemSurveysCountEndpoint import SystemSurveysCountEndpoint
from pywise.endpoints.SystemSurveysInfoEndpoint import SystemSurveysInfoEndpoint
from pywise.models.SurveyModel import SurveyModel

class SystemSurveysEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "surveys", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemSurveysCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemSurveysInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemSurveysIdEndpoint:
        child = SystemSurveysIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SurveyModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SurveyModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SurveyModel]:
        return self._parse_many(SurveyModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SurveyModel:
        return self._parse_one(SurveyModel, super().make_request("POST", params=params))
        