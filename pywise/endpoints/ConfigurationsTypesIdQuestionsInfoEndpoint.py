from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ConfigurationsTypesIdQuestionsInfoCountEndpoint import ConfigurationsTypesIdQuestionsInfoCountEndpoint
from pywise.models.ConfigurationTypeQuestionInfoModel import ConfigurationTypeQuestionInfoModel

class ConfigurationsTypesIdQuestionsInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ConfigurationsTypesIdQuestionsInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ConfigurationTypeQuestionInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ConfigurationTypeQuestionInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ConfigurationTypeQuestionInfoModel]:
        return self._parse_many(ConfigurationTypeQuestionInfoModel, super().make_request("GET", params=params))
        