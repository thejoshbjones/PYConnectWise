from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAgreementsIdAdjustmentsIdEndpoint import FinanceAgreementsIdAdjustmentsIdEndpoint
from pywise.endpoints.FinanceAgreementsIdAdjustmentsCountEndpoint import FinanceAgreementsIdAdjustmentsCountEndpoint
from pywise.models.AdjustmentModel import AdjustmentModel

class FinanceAgreementsIdAdjustmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "adjustments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdAdjustmentsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementsIdAdjustmentsIdEndpoint:
        child = FinanceAgreementsIdAdjustmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AdjustmentModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AdjustmentModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AdjustmentModel]:
        return self._parse_many(AdjustmentModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AdjustmentModel:
        return self._parse_one(AdjustmentModel, super().make_request("POST", params=params))
        