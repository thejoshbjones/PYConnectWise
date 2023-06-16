from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeChargeCodesIdExpenseTypesIdEndpoint import TimeChargeCodesIdExpenseTypesIdEndpoint
from pywise.endpoints.TimeChargeCodesIdExpenseTypesCountEndpoint import TimeChargeCodesIdExpenseTypesCountEndpoint
from pywise.models.ChargeCodeExpenseTypeModel import ChargeCodeExpenseTypeModel

class TimeChargeCodesIdExpenseTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "expenseTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeChargeCodesIdExpenseTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeChargeCodesIdExpenseTypesIdEndpoint:
        child = TimeChargeCodesIdExpenseTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ChargeCodeExpenseTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ChargeCodeExpenseTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ChargeCodeExpenseTypeModel]:
        return self._parse_many(ChargeCodeExpenseTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ChargeCodeExpenseTypeModel:
        return self._parse_one(ChargeCodeExpenseTypeModel, super().make_request("POST", params=params))
        