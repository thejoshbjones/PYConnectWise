from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyMarketDescriptionsIdEndpoint import CompanyMarketDescriptionsIdEndpoint
from pywise.endpoints.CompanyMarketDescriptionsCountEndpoint import CompanyMarketDescriptionsCountEndpoint
from pywise.endpoints.CompanyMarketDescriptionsInfoEndpoint import CompanyMarketDescriptionsInfoEndpoint
from pywise.models.MarketDescriptionModel import MarketDescriptionModel

class CompanyMarketDescriptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "marketDescriptions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyMarketDescriptionsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyMarketDescriptionsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyMarketDescriptionsIdEndpoint:
        child = CompanyMarketDescriptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MarketDescriptionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MarketDescriptionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MarketDescriptionModel]:
        return self._parse_many(MarketDescriptionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MarketDescriptionModel:
        return self._parse_one(MarketDescriptionModel, super().make_request("POST", params=params))
        