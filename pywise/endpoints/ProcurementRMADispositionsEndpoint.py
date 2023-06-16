from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementRMADispositionsIdEndpoint import ProcurementRMADispositionsIdEndpoint
from pywise.endpoints.ProcurementRMADispositionsCountEndpoint import ProcurementRMADispositionsCountEndpoint
from pywise.endpoints.ProcurementRMADispositionsInfoEndpoint import ProcurementRMADispositionsInfoEndpoint
from pywise.models.RmaDispositionModel import RmaDispositionModel

class ProcurementRMADispositionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "RMADispositions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementRMADispositionsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementRMADispositionsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementRMADispositionsIdEndpoint:
        child = ProcurementRMADispositionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[RmaDispositionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            RmaDispositionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[RmaDispositionModel]:
        return self._parse_many(RmaDispositionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> RmaDispositionModel:
        return self._parse_one(RmaDispositionModel, super().make_request("POST", params=params))
        