from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesIdManagementReportNotificationsIdEndpoint import CompanyCompaniesIdManagementReportNotificationsIdEndpoint
from pywise.endpoints.CompanyCompaniesIdManagementReportNotificationsCountEndpoint import CompanyCompaniesIdManagementReportNotificationsCountEndpoint
from pywise.models.ManagementReportNotificationModel import ManagementReportNotificationModel

class CompanyCompaniesIdManagementReportNotificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementReportNotifications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdManagementReportNotificationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesIdManagementReportNotificationsIdEndpoint:
        child = CompanyCompaniesIdManagementReportNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagementReportNotificationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagementReportNotificationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManagementReportNotificationModel]:
        return self._parse_many(ManagementReportNotificationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ManagementReportNotificationModel:
        return self._parse_one(ManagementReportNotificationModel, super().make_request("POST", params=params))
        