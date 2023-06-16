from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementsIdAdditionsIdEndpoint import FinanceAgreementsIdAdditionsIdEndpoint
from pywise.endpoints.FinanceAgreementsIdAdditionsCountEndpoint import FinanceAgreementsIdAdditionsCountEndpoint
from pywise.models.AdditionModel import AdditionModel

class FinanceAgreementsIdAdditionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "additions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdAdditionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementsIdAdditionsIdEndpoint:
        child = FinanceAgreementsIdAdditionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AdditionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AdditionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AdditionModel]:
        return self._parse_many(AdditionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AdditionModel:
        return self._parse_one(AdditionModel, super().make_request("POST", params=params))
        