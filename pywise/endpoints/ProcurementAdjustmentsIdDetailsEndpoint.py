from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementAdjustmentsIdDetailsIdEndpoint import ProcurementAdjustmentsIdDetailsIdEndpoint
from pywise.endpoints.ProcurementAdjustmentsIdDetailsCountEndpoint import ProcurementAdjustmentsIdDetailsCountEndpoint
from pywise.models.AdjustmentDetailModel import AdjustmentDetailModel

class ProcurementAdjustmentsIdDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "details", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementAdjustmentsIdDetailsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementAdjustmentsIdDetailsIdEndpoint:
        child = ProcurementAdjustmentsIdDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AdjustmentDetailModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AdjustmentDetailModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AdjustmentDetailModel]:
        return self._parse_many(AdjustmentDetailModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AdjustmentDetailModel:
        return self._parse_one(AdjustmentDetailModel, super().make_request("POST", params=params))
        