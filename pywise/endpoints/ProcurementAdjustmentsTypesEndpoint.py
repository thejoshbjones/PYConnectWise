from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementAdjustmentsTypesIdEndpoint import ProcurementAdjustmentsTypesIdEndpoint
from pywise.endpoints.ProcurementAdjustmentsTypesCountEndpoint import ProcurementAdjustmentsTypesCountEndpoint
from pywise.endpoints.ProcurementAdjustmentsTypesInfoEndpoint import ProcurementAdjustmentsTypesInfoEndpoint
from pywise.models.AdjustmentTypeModel import AdjustmentTypeModel

class ProcurementAdjustmentsTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementAdjustmentsTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementAdjustmentsTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementAdjustmentsTypesIdEndpoint:
        child = ProcurementAdjustmentsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AdjustmentTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AdjustmentTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AdjustmentTypeModel]:
        return self._parse_many(AdjustmentTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AdjustmentTypeModel:
        return self._parse_one(AdjustmentTypeModel, super().make_request("POST", params=params))
        