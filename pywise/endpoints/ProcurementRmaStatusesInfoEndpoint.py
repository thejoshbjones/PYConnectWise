from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementRmaStatusesInfoCountEndpoint import ProcurementRmaStatusesInfoCountEndpoint
from pywise.models.RmaStatusInfoModel import RmaStatusInfoModel

class ProcurementRmaStatusesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementRmaStatusesInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[RmaStatusInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            RmaStatusInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[RmaStatusInfoModel]:
        return self._parse_many(RmaStatusInfoModel, super().make_request("GET", params=params))
        