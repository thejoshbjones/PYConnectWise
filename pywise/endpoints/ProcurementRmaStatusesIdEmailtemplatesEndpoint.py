from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.RmaStatusEmailTemplateModel import RmaStatusEmailTemplateModel

class ProcurementRmaStatusesIdEmailTemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[RmaStatusEmailTemplateModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            RmaStatusEmailTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[RmaStatusEmailTemplateModel]:
        return self._parse_many(RmaStatusEmailTemplateModel, super().make_request("GET", params=params))
        