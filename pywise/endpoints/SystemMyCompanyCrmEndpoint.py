from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMyCompanyCrmIdEndpoint import SystemMyCompanyCrmIdEndpoint
from pywise.endpoints.SystemMyCompanyCrmCountEndpoint import SystemMyCompanyCrmCountEndpoint
from pywise.endpoints.SystemMyCompanyCrmInfoEndpoint import SystemMyCompanyCrmInfoEndpoint
from pywise.models.CrmModel import CrmModel

class SystemMyCompanyCrmEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "crm", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMyCompanyCrmCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemMyCompanyCrmInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMyCompanyCrmIdEndpoint:
        child = SystemMyCompanyCrmIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CrmModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CrmModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CrmModel]:
        return self._parse_many(CrmModel, super().make_request("GET", params=params))
        