from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.MarketDescriptionInfoModel import MarketDescriptionInfoModel

class CompanyMarketDescriptionsIdInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint, id_index="{id}")
        
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MarketDescriptionInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MarketDescriptionInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> MarketDescriptionInfoModel:
        return self._parse_one(MarketDescriptionInfoModel, super().make_request("GET", params=params))
        