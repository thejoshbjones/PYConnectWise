from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemInfoDepartmentsIdEndpoint import SystemInfoDepartmentsIdEndpoint
from pywise.endpoints.SystemInfoDepartmentsCountEndpoint import SystemInfoDepartmentsCountEndpoint
from pywise.models.DepartmentInfoModel import DepartmentInfoModel

class SystemInfoDepartmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "departments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoDepartmentsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemInfoDepartmentsIdEndpoint:
        child = SystemInfoDepartmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[DepartmentInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            DepartmentInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[DepartmentInfoModel]:
        return self._parse_many(DepartmentInfoModel, super().make_request("GET", params=params))
        