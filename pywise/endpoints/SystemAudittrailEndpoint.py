from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemAudittrailCountEndpoint import SystemAudittrailCountEndpoint
from pywise.models.AuditTrailEntryModel import AuditTrailEntryModel

class SystemAudittrailEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "audittrail", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemAudittrailCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AuditTrailEntryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AuditTrailEntryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AuditTrailEntryModel]:
        return self._parse_many(AuditTrailEntryModel, super().make_request("GET", params=params))
        