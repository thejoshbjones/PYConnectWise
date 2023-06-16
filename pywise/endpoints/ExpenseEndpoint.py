from pywise.endpoints.base.connectwise_top_level_endpoint import ConnectWiseEndpoint
from pywise.endpoints.ExpenseClassificationsEndpoint import ExpenseClassificationsEndpoint
from pywise.endpoints.ExpenseEntriesEndpoint import ExpenseEntriesEndpoint
from pywise.endpoints.ExpensePaymentTypesEndpoint import ExpensePaymentTypesEndpoint
from pywise.endpoints.ExpenseReportsEndpoint import ExpenseReportsEndpoint
from pywise.endpoints.ExpenseTypesEndpoint import ExpenseTypesEndpoint

class ExpenseEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "expense")
        
        self.classifications = self.register_child_endpoint(
            ExpenseClassificationsEndpoint(client, parent_endpoint=self)
        )
        self.entries = self.register_child_endpoint(
            ExpenseEntriesEndpoint(client, parent_endpoint=self)
        )
        self.paymentTypes = self.register_child_endpoint(
            ExpensePaymentTypesEndpoint(client, parent_endpoint=self)
        )
        self.reports = self.register_child_endpoint(
            ExpenseReportsEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            ExpenseTypesEndpoint(client, parent_endpoint=self)
        )