from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementPricingschedulesIdEndpoint import ProcurementPricingschedulesIdEndpoint
from pywise.endpoints.ProcurementPricingschedulesCountEndpoint import ProcurementPricingschedulesCountEndpoint
from pywise.models.PricingScheduleModel import PricingScheduleModel

class ProcurementPricingschedulesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "pricingschedules", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementPricingschedulesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementPricingschedulesIdEndpoint:
        child = ProcurementPricingschedulesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PricingScheduleModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PricingScheduleModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PricingScheduleModel]:
        return self._parse_many(PricingScheduleModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> PricingScheduleModel:
        return self._parse_one(PricingScheduleModel, super().make_request("POST", params=params))
        