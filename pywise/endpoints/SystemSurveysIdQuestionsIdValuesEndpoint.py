from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemSurveysIdQuestionsIdValuesIdEndpoint import SystemSurveysIdQuestionsIdValuesIdEndpoint
from pywise.models.SurveyQuestionValueModel import SurveyQuestionValueModel

class SystemSurveysIdQuestionsIdValuesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "values", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> SystemSurveysIdQuestionsIdValuesIdEndpoint:
        child = SystemSurveysIdQuestionsIdValuesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SurveyQuestionValueModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SurveyQuestionValueModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SurveyQuestionValueModel]:
        return self._parse_many(SurveyQuestionValueModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SurveyQuestionValueModel:
        return self._parse_one(SurveyQuestionValueModel, super().make_request("POST", params=params))
        