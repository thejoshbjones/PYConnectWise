from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyConfigurationsTypesIdQuestionsIdEndpoint import CompanyConfigurationsTypesIdQuestionsIdEndpoint
from pywise.endpoints.CompanyConfigurationsTypesIdQuestionsCountEndpoint import CompanyConfigurationsTypesIdQuestionsCountEndpoint
from pywise.models.ConfigurationTypeQuestionModel import ConfigurationTypeQuestionModel

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
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ConfigurationTypeQuestionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ConfigurationTypeQuestionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ConfigurationTypeQuestionModel]:
        return self._parse_many(ConfigurationTypeQuestionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ConfigurationTypeQuestionModel:
        return self._parse_one(ConfigurationTypeQuestionModel, super().make_request("POST", params=params))
        