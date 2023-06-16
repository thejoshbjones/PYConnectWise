from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceTicketsIdInfoEndpoint import ServiceTicketsIdInfoEndpoint
from pywise.endpoints.ServiceTicketsIdActivitiesEndpoint import ServiceTicketsIdActivitiesEndpoint
from pywise.endpoints.ServiceTicketsIdAllNotesEndpoint import ServiceTicketsIdAllNotesEndpoint
from pywise.endpoints.ServiceTicketsIdAttachChildrenEndpoint import ServiceTicketsIdAttachChildrenEndpoint
from pywise.endpoints.ServiceTicketsIdConfigurationsEndpoint import ServiceTicketsIdConfigurationsEndpoint
from pywise.endpoints.ServiceTicketsIdConvertEndpoint import ServiceTicketsIdConvertEndpoint
from pywise.endpoints.ServiceTicketsIdDocumentsEndpoint import ServiceTicketsIdDocumentsEndpoint
from pywise.endpoints.ServiceTicketsIdMergeEndpoint import ServiceTicketsIdMergeEndpoint
from pywise.endpoints.ServiceTicketsIdNotesEndpoint import ServiceTicketsIdNotesEndpoint
from pywise.endpoints.ServiceTicketsIdProductsEndpoint import ServiceTicketsIdProductsEndpoint
from pywise.endpoints.ServiceTicketsIdScheduleentriesEndpoint import ServiceTicketsIdScheduleentriesEndpoint
from pywise.endpoints.ServiceTicketsIdTasksEndpoint import ServiceTicketsIdTasksEndpoint
from pywise.endpoints.ServiceTicketsIdTimeentriesEndpoint import ServiceTicketsIdTimeentriesEndpoint
from pywise.models.TicketModel import TicketModel

class ServiceTicketsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.info = self.register_child_endpoint(
            ServiceTicketsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.activities = self.register_child_endpoint(
            ServiceTicketsIdActivitiesEndpoint(client, parent_endpoint=self)
        )
        self.allNotes = self.register_child_endpoint(
            ServiceTicketsIdAllNotesEndpoint(client, parent_endpoint=self)
        )
        self.attachChildren = self.register_child_endpoint(
            ServiceTicketsIdAttachChildrenEndpoint(client, parent_endpoint=self)
        )
        self.configurations = self.register_child_endpoint(
            ServiceTicketsIdConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.convert = self.register_child_endpoint(
            ServiceTicketsIdConvertEndpoint(client, parent_endpoint=self)
        )
        self.documents = self.register_child_endpoint(
            ServiceTicketsIdDocumentsEndpoint(client, parent_endpoint=self)
        )
        self.merge = self.register_child_endpoint(
            ServiceTicketsIdMergeEndpoint(client, parent_endpoint=self)
        )
        self.notes = self.register_child_endpoint(
            ServiceTicketsIdNotesEndpoint(client, parent_endpoint=self)
        )
        self.products = self.register_child_endpoint(
            ServiceTicketsIdProductsEndpoint(client, parent_endpoint=self)
        )
        self.scheduleentries = self.register_child_endpoint(
            ServiceTicketsIdScheduleentriesEndpoint(client, parent_endpoint=self)
        )
        self.tasks = self.register_child_endpoint(
            ServiceTicketsIdTasksEndpoint(client, parent_endpoint=self)
        )
        self.timeentries = self.register_child_endpoint(
            ServiceTicketsIdTimeentriesEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TicketModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TicketModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> TicketModel:
        return self._parse_one(TicketModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> TicketModel:
        return self._parse_one(TicketModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> TicketModel:
        return self._parse_one(TicketModel, super().make_request("PATCH", params=params))
        