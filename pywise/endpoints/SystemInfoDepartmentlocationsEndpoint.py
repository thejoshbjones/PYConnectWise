from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemInfoDepartmentlocationsIdEndpoint import SystemInfoDepartmentlocationsIdEndpoint
from pywise.endpoints.SystemInfoDepartmentlocationsCountEndpoint import SystemInfoDepartmentlocationsCountEndpoint
from pywise.models.DepartmentLocationInfoModel import DepartmentLocationInfoModel

class SystemInfoDepartmentlocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "departmentlocations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoDepartmentlocationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemInfoDepartmentlocationsIdEndpoint:
        child = SystemInfoDepartmentlocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[DepartmentLocationInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            DepartmentLocationInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[DepartmentLocationInfoModel]:
        return self._parse_many(DepartmentLocationInfoModel, super().make_request("GET", params=params))
        