from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesOpportunitiesIdConvertToAgreementEndpoint import SalesOpportunitiesIdConvertToAgreementEndpoint
from pywise.endpoints.SalesOpportunitiesIdConvertToProjectEndpoint import SalesOpportunitiesIdConvertToProjectEndpoint
from pywise.endpoints.SalesOpportunitiesIdConvertToSalesOrderEndpoint import SalesOpportunitiesIdConvertToSalesOrderEndpoint
from pywise.endpoints.SalesOpportunitiesIdConvertToServiceTicketEndpoint import SalesOpportunitiesIdConvertToServiceTicketEndpoint
from pywise.endpoints.SalesOpportunitiesIdContactsEndpoint import SalesOpportunitiesIdContactsEndpoint
from pywise.endpoints.SalesOpportunitiesIdForecastEndpoint import SalesOpportunitiesIdForecastEndpoint
from pywise.endpoints.SalesOpportunitiesIdNotesEndpoint import SalesOpportunitiesIdNotesEndpoint
from pywise.endpoints.SalesOpportunitiesIdTeamEndpoint import SalesOpportunitiesIdTeamEndpoint
from pywise.models.OpportunityModel import OpportunityModel

class SalesOpportunitiesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.convertToAgreement = self.register_child_endpoint(
            SalesOpportunitiesIdConvertToAgreementEndpoint(client, parent_endpoint=self)
        )
        self.convertToProject = self.register_child_endpoint(
            SalesOpportunitiesIdConvertToProjectEndpoint(client, parent_endpoint=self)
        )
        self.convertToSalesOrder = self.register_child_endpoint(
            SalesOpportunitiesIdConvertToSalesOrderEndpoint(client, parent_endpoint=self)
        )
        self.convertToServiceTicket = self.register_child_endpoint(
            SalesOpportunitiesIdConvertToServiceTicketEndpoint(client, parent_endpoint=self)
        )
        self.contacts = self.register_child_endpoint(
            SalesOpportunitiesIdContactsEndpoint(client, parent_endpoint=self)
        )
        self.forecast = self.register_child_endpoint(
            SalesOpportunitiesIdForecastEndpoint(client, parent_endpoint=self)
        )
        self.notes = self.register_child_endpoint(
            SalesOpportunitiesIdNotesEndpoint(client, parent_endpoint=self)
        )
        self.team = self.register_child_endpoint(
            SalesOpportunitiesIdTeamEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OpportunityModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OpportunityModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> OpportunityModel:
        return self._parse_one(OpportunityModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> OpportunityModel:
        return self._parse_one(OpportunityModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> OpportunityModel:
        return self._parse_one(OpportunityModel, super().make_request("PATCH", params=params))
        