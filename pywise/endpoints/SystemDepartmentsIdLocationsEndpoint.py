from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemDepartmentsIdLocationsIdEndpoint import SystemDepartmentsIdLocationsIdEndpoint
from pywise.endpoints.SystemDepartmentsIdLocationsCountEndpoint import SystemDepartmentsIdLocationsCountEndpoint
from pywise.models.DepartmentLocationModel import DepartmentLocationModel

class SystemDepartmentsIdLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemDepartmentsIdLocationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemDepartmentsIdLocationsIdEndpoint:
        child = SystemDepartmentsIdLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[DepartmentLocationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            DepartmentLocationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[DepartmentLocationModel]:
        return self._parse_many(DepartmentLocationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> DepartmentLocationModel:
        return self._parse_one(DepartmentLocationModel, super().make_request("POST", params=params))
        