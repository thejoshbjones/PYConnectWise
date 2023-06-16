from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementUnitOfMeasuresIdEndpoint import ProcurementUnitOfMeasuresIdEndpoint
from pywise.endpoints.ProcurementUnitOfMeasuresCountEndpoint import ProcurementUnitOfMeasuresCountEndpoint
from pywise.models.UnitOfMeasureModel import UnitOfMeasureModel

class ProcurementUnitOfMeasuresEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "unitOfMeasures", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementUnitOfMeasuresCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementUnitOfMeasuresIdEndpoint:
        child = ProcurementUnitOfMeasuresIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[UnitOfMeasureModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            UnitOfMeasureModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[UnitOfMeasureModel]:
        return self._parse_many(UnitOfMeasureModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> UnitOfMeasureModel:
        return self._parse_one(UnitOfMeasureModel, super().make_request("POST", params=params))
        