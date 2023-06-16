from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceSurveysIdQuestionsIdEndpoint import ServiceSurveysIdQuestionsIdEndpoint
from pywise.endpoints.ServiceSurveysIdQuestionsCountEndpoint import ServiceSurveysIdQuestionsCountEndpoint
from pywise.models.ServiceSurveyQuestionModel import ServiceSurveyQuestionModel

class ServiceSurveysIdQuestionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "questions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceSurveysIdQuestionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceSurveysIdQuestionsIdEndpoint:
        child = ServiceSurveysIdQuestionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ServiceSurveyQuestionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ServiceSurveyQuestionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ServiceSurveyQuestionModel]:
        return self._parse_many(ServiceSurveyQuestionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ServiceSurveyQuestionModel:
        return self._parse_one(ServiceSurveyQuestionModel, super().make_request("POST", params=params))
        