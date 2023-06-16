from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementAdjustmentsIdEndpoint import ProcurementAdjustmentsIdEndpoint
from pywise.endpoints.ProcurementAdjustmentsCountEndpoint import ProcurementAdjustmentsCountEndpoint
from pywise.endpoints.ProcurementAdjustmentsTypesEndpoint import ProcurementAdjustmentsTypesEndpoint
from pywise.models.ProcurementAdjustmentModel import ProcurementAdjustmentModel

class ProcurementAdjustmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "adjustments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementAdjustmentsCountEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            ProcurementAdjustmentsTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementAdjustmentsIdEndpoint:
        child = ProcurementAdjustmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProcurementAdjustmentModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProcurementAdjustmentModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProcurementAdjustmentModel]:
        return self._parse_many(ProcurementAdjustmentModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProcurementAdjustmentModel:
        return self._parse_one(ProcurementAdjustmentModel, super().make_request("POST", params=params))
        