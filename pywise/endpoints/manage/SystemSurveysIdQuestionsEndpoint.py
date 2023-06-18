from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemSurveysIdQuestionsIdEndpoint import SystemSurveysIdQuestionsIdEndpoint
from pywise.endpoints.manage.SystemSurveysIdQuestionsCountEndpoint import SystemSurveysIdQuestionsCountEndpoint
from pywise.models.manage.SurveyQuestionModel import SurveyQuestionModel

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
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SurveyQuestionModel]:
        """
        Performs a GET request against the /system/surveys/{parentId}/questions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SurveyQuestionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SurveyQuestionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SurveyQuestionModel]:
        """
        Performs a GET request against the /system/surveys/{parentId}/questions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SurveyQuestionModel]: The parsed response data.
        """
        return self._parse_many(SurveyQuestionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SurveyQuestionModel:
        """
        Performs a POST request against the /system/surveys/{parentId}/questions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyQuestionModel: The parsed response data.
        """
        return self._parse_one(SurveyQuestionModel, super().make_request("POST", params=params).json())
        