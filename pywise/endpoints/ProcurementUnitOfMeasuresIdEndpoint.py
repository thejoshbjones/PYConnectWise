from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementUnitOfMeasuresIdConversionsEndpoint import ProcurementUnitOfMeasuresIdConversionsEndpoint
from pywise.models.UnitOfMeasureModel import UnitOfMeasureModel

class ProcurementUnitOfMeasuresIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.conversions = self.register_child_endpoint(
            ProcurementUnitOfMeasuresIdConversionsEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> UnitOfMeasureModel:
        return self._parse_one(UnitOfMeasureModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> UnitOfMeasureModel:
        return self._parse_one(UnitOfMeasureModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> UnitOfMeasureModel:
        return self._parse_one(UnitOfMeasureModel, super().make_request("PATCH", params=params))
        