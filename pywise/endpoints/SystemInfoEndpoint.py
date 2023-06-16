from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemInfoDepartmentlocationsEndpoint import SystemInfoDepartmentlocationsEndpoint
from pywise.endpoints.SystemInfoDepartmentsEndpoint import SystemInfoDepartmentsEndpoint
from pywise.endpoints.SystemInfoLinksEndpoint import SystemInfoLinksEndpoint
from pywise.endpoints.SystemInfoLocalesEndpoint import SystemInfoLocalesEndpoint
from pywise.endpoints.SystemInfoLocationsEndpoint import SystemInfoLocationsEndpoint
from pywise.endpoints.SystemInfoMembersEndpoint import SystemInfoMembersEndpoint
from pywise.endpoints.SystemInfoPersonasEndpoint import SystemInfoPersonasEndpoint
from pywise.endpoints.SystemInfoStandardNotesEndpoint import SystemInfoStandardNotesEndpoint
from pywise.models.InfoModel import InfoModel

class SystemInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.departmentlocations = self.register_child_endpoint(
            SystemInfoDepartmentlocationsEndpoint(client, parent_endpoint=self)
        )
        self.departments = self.register_child_endpoint(
            SystemInfoDepartmentsEndpoint(client, parent_endpoint=self)
        )
        self.links = self.register_child_endpoint(
            SystemInfoLinksEndpoint(client, parent_endpoint=self)
        )
        self.locales = self.register_child_endpoint(
            SystemInfoLocalesEndpoint(client, parent_endpoint=self)
        )
        self.locations = self.register_child_endpoint(
            SystemInfoLocationsEndpoint(client, parent_endpoint=self)
        )
        self.members = self.register_child_endpoint(
            SystemInfoMembersEndpoint(client, parent_endpoint=self)
        )
        self.personas = self.register_child_endpoint(
            SystemInfoPersonasEndpoint(client, parent_endpoint=self)
        )
        self.standardNotes = self.register_child_endpoint(
            SystemInfoStandardNotesEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[InfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            InfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> InfoModel:
        return self._parse_one(InfoModel, super().make_request("GET", params=params))
        