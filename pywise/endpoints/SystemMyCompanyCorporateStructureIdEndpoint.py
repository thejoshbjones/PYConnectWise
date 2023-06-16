from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMyCompanyCorporateStructureIdInfoEndpoint import SystemMyCompanyCorporateStructureIdInfoEndpoint
from pywise.models.CorporateStructureModel import CorporateStructureModel

class SystemMyCompanyCorporateStructureIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.info = self.register_child_endpoint(
            SystemMyCompanyCorporateStructureIdInfoEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CorporateStructureModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CorporateStructureModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> CorporateStructureModel:
        return self._parse_one(CorporateStructureModel, super().make_request("GET", params=params))
        
    def put(self, data=None, params=None) -> CorporateStructureModel:
        return self._parse_one(CorporateStructureModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> CorporateStructureModel:
        return self._parse_one(CorporateStructureModel, super().make_request("PATCH", params=params))
        