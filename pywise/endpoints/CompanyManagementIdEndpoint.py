from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyManagementIdExecuteManagedItSyncEndpoint import CompanyManagementIdExecuteManagedItSyncEndpoint
from pywise.endpoints.CompanyManagementIdLogsEndpoint import CompanyManagementIdLogsEndpoint
from pywise.endpoints.CompanyManagementIdManagementReportNotificationsEndpoint import CompanyManagementIdManagementReportNotificationsEndpoint
from pywise.models.ManagementModel import ManagementModel

class CompanyManagementIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.executeManagedItSync = self.register_child_endpoint(
            CompanyManagementIdExecuteManagedItSyncEndpoint(client, parent_endpoint=self)
        )
        self.logs = self.register_child_endpoint(
            CompanyManagementIdLogsEndpoint(client, parent_endpoint=self)
        )
        self.managementReportNotifications = self.register_child_endpoint(
            CompanyManagementIdManagementReportNotificationsEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagementModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagementModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> ManagementModel:
        return self._parse_one(ManagementModel, super().make_request("GET", params=params))
        
    def put(self, data=None, params=None) -> ManagementModel:
        return self._parse_one(ManagementModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> ManagementModel:
        return self._parse_one(ManagementModel, super().make_request("PATCH", params=params))
        