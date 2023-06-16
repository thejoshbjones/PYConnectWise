from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemSurveysIdQuestionsIdEndpoint import SystemSurveysIdQuestionsIdEndpoint
from pywise.endpoints.SystemSurveysIdQuestionsCountEndpoint import SystemSurveysIdQuestionsCountEndpoint
from pywise.models.SurveyQuestionModel import SurveyQuestionModel

class SystemSurveysIdQuestionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "questions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemSurveysIdQuestionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemSurveysIdQuestionsIdEndpoint:
        child = SystemSurveysIdQuestionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SurveyQuestionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SurveyQuestionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SurveyQuestionModel]:
        return self._parse_many(SurveyQuestionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SurveyQuestionModel:
        return self._parse_one(SurveyQuestionModel, super().make_request("POST", params=params))
        