from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemDepartmentsIdEndpoint import SystemDepartmentsIdEndpoint
from pywise.endpoints.SystemDepartmentsCountEndpoint import SystemDepartmentsCountEndpoint
from pywise.models.DepartmentModel import DepartmentModel

class SystemDepartmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "departments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemDepartmentsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemDepartmentsIdEndpoint:
        child = SystemDepartmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[DepartmentModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            DepartmentModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[DepartmentModel]:
        return self._parse_many(DepartmentModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> DepartmentModel:
        return self._parse_one(DepartmentModel, super().make_request("POST", params=params))
        