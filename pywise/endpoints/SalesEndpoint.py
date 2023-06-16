from pywise.endpoints.base.connectwise_top_level_endpoint import ConnectWiseEndpoint
from pywise.endpoints.SalesActivitiesEndpoint import SalesActivitiesEndpoint
from pywise.endpoints.SalesCommissionsEndpoint import SalesCommissionsEndpoint
from pywise.endpoints.SalesOpportunitiesEndpoint import SalesOpportunitiesEndpoint
from pywise.endpoints.SalesOrdersEndpoint import SalesOrdersEndpoint
from pywise.endpoints.SalesProbabilitiesEndpoint import SalesProbabilitiesEndpoint
from pywise.endpoints.SalesQuotasEndpoint import SalesQuotasEndpoint
from pywise.endpoints.SalesRolesEndpoint import SalesRolesEndpoint
from pywise.endpoints.SalesSalesTeamsEndpoint import SalesSalesTeamsEndpoint
from pywise.endpoints.SalesStagesEndpoint import SalesStagesEndpoint

class SalesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "sales")
        
        self.activities = self.register_child_endpoint(
            SalesActivitiesEndpoint(client, parent_endpoint=self)
        )
        self.commissions = self.register_child_endpoint(
            SalesCommissionsEndpoint(client, parent_endpoint=self)
        )
        self.opportunities = self.register_child_endpoint(
            SalesOpportunitiesEndpoint(client, parent_endpoint=self)
        )
        self.orders = self.register_child_endpoint(
            SalesOrdersEndpoint(client, parent_endpoint=self)
        )
        self.probabilities = self.register_child_endpoint(
            SalesProbabilitiesEndpoint(client, parent_endpoint=self)
        )
        self.quotas = self.register_child_endpoint(
            SalesQuotasEndpoint(client, parent_endpoint=self)
        )
        self.roles = self.register_child_endpoint(
            SalesRolesEndpoint(client, parent_endpoint=self)
        )
        self.salesTeams = self.register_child_endpoint(
            SalesSalesTeamsEndpoint(client, parent_endpoint=self)
        )
        self.stages = self.register_child_endpoint(
            SalesStagesEndpoint(client, parent_endpoint=self)
        )