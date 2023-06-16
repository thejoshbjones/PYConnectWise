from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeInfoChargeCodeExpenseTypesCountEndpoint import TimeInfoChargeCodeExpenseTypesCountEndpoint
from pywise.models.ChargeCodeExpenseTypeModel import ChargeCodeExpenseTypeModel

class TimeInfoChargeCodeExpenseTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "chargeCodeExpenseTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeInfoChargeCodeExpenseTypesCountEndpoint(client, parent_endpoint=self)
        )
    
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
        