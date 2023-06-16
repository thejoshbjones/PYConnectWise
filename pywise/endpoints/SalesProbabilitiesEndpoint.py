from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesProbabilitiesIdEndpoint import SalesProbabilitiesIdEndpoint
from pywise.endpoints.SalesProbabilitiesCountEndpoint import SalesProbabilitiesCountEndpoint
from pywise.endpoints.SalesProbabilitiesInfoEndpoint import SalesProbabilitiesInfoEndpoint
from pywise.models.SalesProbabilityModel import SalesProbabilityModel

class SalesProbabilitiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "probabilities", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesProbabilitiesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SalesProbabilitiesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesProbabilitiesIdEndpoint:
        child = SalesProbabilitiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SalesProbabilityModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SalesProbabilityModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SalesProbabilityModel]:
        return self._parse_many(SalesProbabilityModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SalesProbabilityModel:
        return self._parse_one(SalesProbabilityModel, super().make_request("POST", params=params))
        