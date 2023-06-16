from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementPricingschedulesIdDetailsIdEndpoint import ProcurementPricingschedulesIdDetailsIdEndpoint
from pywise.endpoints.ProcurementPricingschedulesIdDetailsCountEndpoint import ProcurementPricingschedulesIdDetailsCountEndpoint
from pywise.models.PricingDetailModel import PricingDetailModel

class ProcurementPricingschedulesIdDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "details", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementPricingschedulesIdDetailsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementPricingschedulesIdDetailsIdEndpoint:
        child = ProcurementPricingschedulesIdDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PricingDetailModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PricingDetailModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PricingDetailModel]:
        return self._parse_many(PricingDetailModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> PricingDetailModel:
        return self._parse_one(PricingDetailModel, super().make_request("POST", params=params))
        