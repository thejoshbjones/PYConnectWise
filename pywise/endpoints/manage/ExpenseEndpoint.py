from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.endpoints.manage.ExpenseClassificationsEndpoint import ExpenseClassificationsEndpoint
from pywise.endpoints.manage.ExpenseEntriesEndpoint import ExpenseEntriesEndpoint
from pywise.endpoints.manage.ExpensePaymentTypesEndpoint import ExpensePaymentTypesEndpoint
from pywise.endpoints.manage.ExpenseReportsEndpoint import ExpenseReportsEndpoint
from pywise.endpoints.manage.ExpenseTypesEndpoint import ExpenseTypesEndpoint

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