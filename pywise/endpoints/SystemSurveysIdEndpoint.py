from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemSurveysIdCopyEndpoint import SystemSurveysIdCopyEndpoint
from pywise.endpoints.SystemSurveysIdInfoEndpoint import SystemSurveysIdInfoEndpoint
from pywise.endpoints.SystemSurveysIdQuestionsEndpoint import SystemSurveysIdQuestionsEndpoint
from pywise.models.SurveyModel import SurveyModel

class SystemSurveysIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.copy = self.register_child_endpoint(
            SystemSurveysIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemSurveysIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.questions = self.register_child_endpoint(
            SystemSurveysIdQuestionsEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> SurveyModel:
        return self._parse_one(SurveyModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> SurveyModel:
        return self._parse_one(SurveyModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> SurveyModel:
        return self._parse_one(SurveyModel, super().make_request("PATCH", params=params))
        