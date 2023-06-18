from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SalesOpportunitiesIdConvertToAgreementEndpoint import SalesOpportunitiesIdConvertToAgreementEndpoint
from pywise.endpoints.manage.SalesOpportunitiesIdConvertToProjectEndpoint import SalesOpportunitiesIdConvertToProjectEndpoint
from pywise.endpoints.manage.SalesOpportunitiesIdConvertToSalesOrderEndpoint import SalesOpportunitiesIdConvertToSalesOrderEndpoint
from pywise.endpoints.manage.SalesOpportunitiesIdConvertToServiceTicketEndpoint import SalesOpportunitiesIdConvertToServiceTicketEndpoint
from pywise.endpoints.manage.SalesOpportunitiesIdContactsEndpoint import SalesOpportunitiesIdContactsEndpoint
from pywise.endpoints.manage.SalesOpportunitiesIdForecastEndpoint import SalesOpportunitiesIdForecastEndpoint
from pywise.endpoints.manage.SalesOpportunitiesIdNotesEndpoint import SalesOpportunitiesIdNotesEndpoint
from pywise.endpoints.manage.SalesOpportunitiesIdTeamEndpoint import SalesOpportunitiesIdTeamEndpoint
from pywise.models.manage.OpportunityModel import OpportunityModel

class SalesOpportunitiesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
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
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OpportunityModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            OpportunityModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityModel:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityModel: The parsed response data.
        """
        return self._parse_one(OpportunityModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityModel:
        """
        Performs a PUT request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityModel: The parsed response data.
        """
        return self._parse_one(OpportunityModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityModel:
        """
        Performs a PATCH request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityModel: The parsed response data.
        """
        return self._parse_one(OpportunityModel, super().make_request("PATCH", params=params).json())
        