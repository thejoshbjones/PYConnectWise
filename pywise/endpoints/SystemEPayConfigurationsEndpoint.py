from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemEPayConfigurationsIdEndpoint import SystemEPayConfigurationsIdEndpoint
from pywise.endpoints.SystemEPayConfigurationsCountEndpoint import SystemEPayConfigurationsCountEndpoint
from pywise.models.EPayConfigurationModel import EPayConfigurationModel

class SystemEPayConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ePayConfigurations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemEPayConfigurationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemEPayConfigurationsIdEndpoint:
        child = SystemEPayConfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[EPayConfigurationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            EPayConfigurationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[EPayConfigurationModel]:
        return self._parse_many(EPayConfigurationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> EPayConfigurationModel:
        return self._parse_one(EPayConfigurationModel, super().make_request("POST", params=params))
        