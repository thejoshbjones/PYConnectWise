from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServiceSurveysIdQuestionsIdEndpoint import ServiceSurveysIdQuestionsIdEndpoint
from pywise.endpoints.manage.ServiceSurveysIdQuestionsCountEndpoint import ServiceSurveysIdQuestionsCountEndpoint
from pywise.models.manage.ServiceSurveyQuestionModel import ServiceSurveyQuestionModel

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
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceSurveyQuestionModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceSurveyQuestionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ServiceSurveyQuestionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceSurveyQuestionModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceSurveyQuestionModel]: The parsed response data.
        """
        return self._parse_many(ServiceSurveyQuestionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceSurveyQuestionModel:
        """
        Performs a POST request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyQuestionModel: The parsed response data.
        """
        return self._parse_one(ServiceSurveyQuestionModel, super().make_request("POST", params=params).json())
        