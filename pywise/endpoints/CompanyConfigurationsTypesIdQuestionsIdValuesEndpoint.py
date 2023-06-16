from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint import CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint
from pywise.endpoints.CompanyConfigurationsTypesIdQuestionsIdValuesCountEndpoint import CompanyConfigurationsTypesIdQuestionsIdValuesCountEndpoint
from pywise.models.ConfigurationTypeQuestionValueModel import ConfigurationTypeQuestionValueModel

class CompanyConfigurationsTypesIdQuestionsIdValuesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "values", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyConfigurationsTypesIdQuestionsIdValuesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint:
        child = CompanyConfigurationsTypesIdQuestionsIdValuesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ConfigurationTypeQuestionValueModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ConfigurationTypeQuestionValueModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ConfigurationTypeQuestionValueModel]:
        return self._parse_many(ConfigurationTypeQuestionValueModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ConfigurationTypeQuestionValueModel:
        return self._parse_one(ConfigurationTypeQuestionValueModel, super().make_request("POST", params=params))
        