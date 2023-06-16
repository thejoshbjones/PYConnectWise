from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemLocationsIdDepartmentsIdEndpoint import SystemLocationsIdDepartmentsIdEndpoint
from pywise.endpoints.SystemLocationsIdDepartmentsCountEndpoint import SystemLocationsIdDepartmentsCountEndpoint
from pywise.models.LocationDepartmentModel import LocationDepartmentModel

class SystemLocationsIdDepartmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "departments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemLocationsIdDepartmentsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemLocationsIdDepartmentsIdEndpoint:
        child = SystemLocationsIdDepartmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[LocationDepartmentModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            LocationDepartmentModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[LocationDepartmentModel]:
        return self._parse_many(LocationDepartmentModel, super().make_request("GET", params=params))
        