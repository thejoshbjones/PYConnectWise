from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.ConfigurationModel import ConfigurationModel
from pywise.models.BulkResultModel import BulkResultModel

class CompanyConfigurationsBulkEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "bulk", parent_endpoint=parent_endpoint)
        
    
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
    
    def post(self, data=None, params=None) -> ConfigurationModel:
        return self._parse_one(ConfigurationModel, super().make_request("POST", params=params))
        
    def delete(self, data=None, params=None) -> BulkResultModel:
        return self._parse_one(BulkResultModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> ConfigurationModel:
        return self._parse_one(ConfigurationModel, super().make_request("PUT", params=params))
        