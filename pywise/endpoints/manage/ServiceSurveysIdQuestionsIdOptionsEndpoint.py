from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ServiceSurveysIdQuestionsIdOptionsIdEndpoint import ServiceSurveysIdQuestionsIdOptionsIdEndpoint
from pywise.endpoints.manage.ServiceSurveysIdQuestionsIdOptionsCountEndpoint import ServiceSurveysIdQuestionsIdOptionsCountEndpoint
from pywise.models.manage.SurveyOptionModel import SurveyOptionModel

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
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SurveyOptionModel]:
        """
        Performs a GET request against the /service/surveys/{grandparentId}/questions/{parentId}/options endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SurveyOptionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SurveyOptionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SurveyOptionModel]:
        """
        Performs a GET request against the /service/surveys/{grandparentId}/questions/{parentId}/options endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SurveyOptionModel]: The parsed response data.
        """
        return self._parse_many(SurveyOptionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SurveyOptionModel:
        """
        Performs a POST request against the /service/surveys/{grandparentId}/questions/{parentId}/options endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyOptionModel: The parsed response data.
        """
        return self._parse_one(SurveyOptionModel, super().make_request("POST", params=params).json())
        