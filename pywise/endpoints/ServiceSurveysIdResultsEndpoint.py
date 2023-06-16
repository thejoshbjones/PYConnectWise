from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceSurveysIdResultsIdEndpoint import ServiceSurveysIdResultsIdEndpoint
from pywise.endpoints.ServiceSurveysIdResultsCountEndpoint import ServiceSurveysIdResultsCountEndpoint
from pywise.models.SurveyResultModel import SurveyResultModel

class ServiceSurveysIdResultsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "results", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceSurveysIdResultsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceSurveysIdResultsIdEndpoint:
        child = ServiceSurveysIdResultsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SurveyResultModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SurveyResultModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SurveyResultModel]:
        return self._parse_many(SurveyResultModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SurveyResultModel:
        return self._parse_one(SurveyResultModel, super().make_request("POST", params=params))
        