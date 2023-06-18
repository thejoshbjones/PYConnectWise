from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyConfigurationsTypesIdQuestionsIdEndpoint import CompanyConfigurationsTypesIdQuestionsIdEndpoint
from pywise.endpoints.manage.CompanyConfigurationsTypesIdQuestionsCountEndpoint import CompanyConfigurationsTypesIdQuestionsCountEndpoint
from pywise.models.manage.ConfigurationTypeQuestionModel import ConfigurationTypeQuestionModel

class CompanyConfigurationsTypesIdQuestionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "questions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyConfigurationsTypesIdQuestionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyConfigurationsTypesIdQuestionsIdEndpoint:
        child = CompanyConfigurationsTypesIdQuestionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ConfigurationTypeQuestionModel]:
        """
        Performs a GET request against the /company/configurations/types/{parentId}/questions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationTypeQuestionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ConfigurationTypeQuestionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ConfigurationTypeQuestionModel]:
        """
        Performs a GET request against the /company/configurations/types/{parentId}/questions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationTypeQuestionModel]: The parsed response data.
        """
        return self._parse_many(ConfigurationTypeQuestionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ConfigurationTypeQuestionModel:
        """
        Performs a POST request against the /company/configurations/types/{parentId}/questions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationTypeQuestionModel: The parsed response data.
        """
        return self._parse_one(ConfigurationTypeQuestionModel, super().make_request("POST", params=params).json())
        