from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyManagementBackupsIdEndpoint import CompanyManagementBackupsIdEndpoint
from pywise.endpoints.CompanyManagementBackupsCountEndpoint import CompanyManagementBackupsCountEndpoint
from pywise.models.ManagementBackupModel import ManagementBackupModel

class CompanyManagementBackupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementBackups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagementBackupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyManagementBackupsIdEndpoint:
        child = CompanyManagementBackupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagementBackupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagementBackupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManagementBackupModel]:
        return self._parse_many(ManagementBackupModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ManagementBackupModel:
        return self._parse_one(ManagementBackupModel, super().make_request("POST", params=params))
        