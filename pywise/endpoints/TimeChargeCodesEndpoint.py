from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeChargeCodesIdEndpoint import TimeChargeCodesIdEndpoint
from pywise.endpoints.TimeChargeCodesCountEndpoint import TimeChargeCodesCountEndpoint
from pywise.endpoints.TimeChargeCodesInfoEndpoint import TimeChargeCodesInfoEndpoint
from pywise.models.ChargeCodeModel import ChargeCodeModel

class TimeChargeCodesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "chargeCodes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeChargeCodesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            TimeChargeCodesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeChargeCodesIdEndpoint:
        child = TimeChargeCodesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ChargeCodeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ChargeCodeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ChargeCodeModel]:
        return self._parse_many(ChargeCodeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ChargeCodeModel:
        return self._parse_one(ChargeCodeModel, super().make_request("POST", params=params))
        