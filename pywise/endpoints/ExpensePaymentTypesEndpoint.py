from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ExpensePaymentTypesIdEndpoint import ExpensePaymentTypesIdEndpoint
from pywise.endpoints.ExpensePaymentTypesCountEndpoint import ExpensePaymentTypesCountEndpoint
from pywise.endpoints.ExpensePaymentTypesInfoEndpoint import ExpensePaymentTypesInfoEndpoint
from pywise.models.PaymentTypeModel import PaymentTypeModel

class ExpensePaymentTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "paymentTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ExpensePaymentTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ExpensePaymentTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ExpensePaymentTypesIdEndpoint:
        child = ExpensePaymentTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PaymentTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PaymentTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PaymentTypeModel]:
        return self._parse_many(PaymentTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> PaymentTypeModel:
        return self._parse_one(PaymentTypeModel, super().make_request("POST", params=params))
        