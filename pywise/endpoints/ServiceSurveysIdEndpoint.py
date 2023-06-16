from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceSurveysIdCopyEndpoint import ServiceSurveysIdCopyEndpoint
from pywise.endpoints.ServiceSurveysIdUsagesEndpoint import ServiceSurveysIdUsagesEndpoint
from pywise.endpoints.ServiceSurveysIdQuestionsEndpoint import ServiceSurveysIdQuestionsEndpoint
from pywise.endpoints.ServiceSurveysIdResultsEndpoint import ServiceSurveysIdResultsEndpoint
from pywise.models.ServiceSurveyModel import ServiceSurveyModel

class ServiceSurveysIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.copy = self.register_child_endpoint(
            ServiceSurveysIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            ServiceSurveysIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.questions = self.register_child_endpoint(
            ServiceSurveysIdQuestionsEndpoint(client, parent_endpoint=self)
        )
        self.results = self.register_child_endpoint(
            ServiceSurveysIdResultsEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ServiceSurveyModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ServiceSurveyModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> ServiceSurveyModel:
        return self._parse_one(ServiceSurveyModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> ServiceSurveyModel:
        return self._parse_one(ServiceSurveyModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> ServiceSurveyModel:
        return self._parse_one(ServiceSurveyModel, super().make_request("PATCH", params=params))
        