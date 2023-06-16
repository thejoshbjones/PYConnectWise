from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemLocationsIdUsagesEndpoint import SystemLocationsIdUsagesEndpoint
from pywise.endpoints.SystemLocationsIdDepartmentsEndpoint import SystemLocationsIdDepartmentsEndpoint
from pywise.endpoints.SystemLocationsIdWorkRolesEndpoint import SystemLocationsIdWorkRolesEndpoint
from pywise.models.LocationModel import LocationModel

class SystemLocationsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.usages = self.register_child_endpoint(
            SystemLocationsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.departments = self.register_child_endpoint(
            SystemLocationsIdDepartmentsEndpoint(client, parent_endpoint=self)
        )
        self.workRoles = self.register_child_endpoint(
            SystemLocationsIdWorkRolesEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[LocationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            LocationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> LocationModel:
        return self._parse_one(LocationModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> LocationModel:
        return self._parse_one(LocationModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> LocationModel:
        return self._parse_one(LocationModel, super().make_request("PATCH", params=params))
        