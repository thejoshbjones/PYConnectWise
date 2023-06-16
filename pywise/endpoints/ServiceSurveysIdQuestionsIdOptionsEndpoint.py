from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceSurveysIdQuestionsIdOptionsIdEndpoint import ServiceSurveysIdQuestionsIdOptionsIdEndpoint
from pywise.endpoints.ServiceSurveysIdQuestionsIdOptionsCountEndpoint import ServiceSurveysIdQuestionsIdOptionsCountEndpoint
from pywise.models.SurveyOptionModel import SurveyOptionModel

class ServiceSurveysIdQuestionsIdOptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "options", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceSurveysIdQuestionsIdOptionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceSurveysIdQuestionsIdOptionsIdEndpoint:
        child = ServiceSurveysIdQuestionsIdOptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SurveyOptionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SurveyOptionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SurveyOptionModel]:
        return self._parse_many(SurveyOptionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SurveyOptionModel:
        return self._parse_one(SurveyOptionModel, super().make_request("POST", params=params))
        