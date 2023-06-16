from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMyCompanyCorporateStructureLevelsIdEndpoint import SystemMyCompanyCorporateStructureLevelsIdEndpoint
from pywise.endpoints.SystemMyCompanyCorporateStructureLevelsCountEndpoint import SystemMyCompanyCorporateStructureLevelsCountEndpoint
from pywise.models.CorporateStructureLevelModel import CorporateStructureLevelModel

class SystemMyCompanyCorporateStructureLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "corporateStructureLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMyCompanyCorporateStructureLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMyCompanyCorporateStructureLevelsIdEndpoint:
        child = SystemMyCompanyCorporateStructureLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CorporateStructureLevelModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CorporateStructureLevelModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CorporateStructureLevelModel]:
        return self._parse_many(CorporateStructureLevelModel, super().make_request("GET", params=params))
        