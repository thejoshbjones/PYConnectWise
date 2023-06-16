from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMyCompanyCorporateStructureIdEndpoint import SystemMyCompanyCorporateStructureIdEndpoint
from pywise.endpoints.SystemMyCompanyCorporateStructureCountEndpoint import SystemMyCompanyCorporateStructureCountEndpoint
from pywise.endpoints.SystemMyCompanyCorporateStructureInfoEndpoint import SystemMyCompanyCorporateStructureInfoEndpoint
from pywise.models.CorporateStructureModel import CorporateStructureModel

class SystemMyCompanyCorporateStructureEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "corporateStructure", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMyCompanyCorporateStructureCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemMyCompanyCorporateStructureInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMyCompanyCorporateStructureIdEndpoint:
        child = SystemMyCompanyCorporateStructureIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
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
    
    def get(self, data=None, params=None) -> list[CorporateStructureModel]:
        return self._parse_many(CorporateStructureModel, super().make_request("GET", params=params))
        