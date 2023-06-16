from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint import ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint
from pywise.endpoints.ProcurementPricingschedulesIdDetailsIdBreaksCountEndpoint import ProcurementPricingschedulesIdDetailsIdBreaksCountEndpoint
from pywise.models.PricingBreakModel import PricingBreakModel

class ProcurementPricingschedulesIdDetailsIdBreaksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "breaks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementPricingschedulesIdDetailsIdBreaksCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint:
        child = ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PricingBreakModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PricingBreakModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PricingBreakModel]:
        return self._parse_many(PricingBreakModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> PricingBreakModel:
        return self._parse_one(PricingBreakModel, super().make_request("POST", params=params))
        