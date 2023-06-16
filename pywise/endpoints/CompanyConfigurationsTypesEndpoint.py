from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyConfigurationsTypesIdEndpoint import CompanyConfigurationsTypesIdEndpoint
from pywise.endpoints.CompanyConfigurationsTypesCountEndpoint import CompanyConfigurationsTypesCountEndpoint
from pywise.models.ConfigurationTypeModel import ConfigurationTypeModel

class CompanyConfigurationsTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyConfigurationsTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyConfigurationsTypesIdEndpoint:
        child = CompanyConfigurationsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ConfigurationTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ConfigurationTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ConfigurationTypeModel]:
        return self._parse_many(ConfigurationTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ConfigurationTypeModel:
        return self._parse_one(ConfigurationTypeModel, super().make_request("POST", params=params))
        