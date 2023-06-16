from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementsIdConfigurationsIdEndpoint import FinanceAgreementsIdConfigurationsIdEndpoint
from pywise.endpoints.FinanceAgreementsIdConfigurationsCountEndpoint import FinanceAgreementsIdConfigurationsCountEndpoint
from pywise.models.ConfigurationReferenceModel import ConfigurationReferenceModel

class FinanceAgreementsIdConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "configurations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdConfigurationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementsIdConfigurationsIdEndpoint:
        child = FinanceAgreementsIdConfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ConfigurationReferenceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ConfigurationReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ConfigurationReferenceModel]:
        return self._parse_many(ConfigurationReferenceModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ConfigurationReferenceModel:
        return self._parse_one(ConfigurationReferenceModel, super().make_request("POST", params=params))
        