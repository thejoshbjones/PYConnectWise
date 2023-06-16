from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceSurveysIdEndpoint import ServiceSurveysIdEndpoint
from pywise.endpoints.ServiceSurveysCountEndpoint import ServiceSurveysCountEndpoint
from pywise.models.ServiceSurveyModel import ServiceSurveyModel

class ServiceSurveysEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "surveys", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceSurveysCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceSurveysIdEndpoint:
        child = ServiceSurveysIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
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
    
    def get(self, data=None, params=None) -> list[ServiceSurveyModel]:
        return self._parse_many(ServiceSurveyModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ServiceSurveyModel:
        return self._parse_one(ServiceSurveyModel, super().make_request("POST", params=params))
        