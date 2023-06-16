from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyConfigurationsIdEndpoint import CompanyConfigurationsIdEndpoint
from pywise.endpoints.CompanyConfigurationsBulkEndpoint import CompanyConfigurationsBulkEndpoint
from pywise.endpoints.CompanyConfigurationsCountEndpoint import CompanyConfigurationsCountEndpoint
from pywise.endpoints.CompanyConfigurationsStatusesEndpoint import CompanyConfigurationsStatusesEndpoint
from pywise.endpoints.CompanyConfigurationsTypesEndpoint import CompanyConfigurationsTypesEndpoint
from pywise.models.ConfigurationModel import ConfigurationModel

class CompanyConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "configurations", parent_endpoint=parent_endpoint)
        
        self.bulk = self.register_child_endpoint(
            CompanyConfigurationsBulkEndpoint(client, parent_endpoint=self)
        )
        self.count = self.register_child_endpoint(
            CompanyConfigurationsCountEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            CompanyConfigurationsStatusesEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            CompanyConfigurationsTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyConfigurationsIdEndpoint:
        child = CompanyConfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ConfigurationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ConfigurationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ConfigurationModel]:
        return self._parse_many(ConfigurationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ConfigurationModel:
        return self._parse_one(ConfigurationModel, super().make_request("POST", params=params))
        