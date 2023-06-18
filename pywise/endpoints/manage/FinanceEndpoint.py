from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.endpoints.manage.FinanceAccountingPackagesEndpoint import FinanceAccountingPackagesEndpoint
from pywise.endpoints.manage.FinanceAccountingPackageSetupEndpoint import FinanceAccountingPackageSetupEndpoint
from pywise.endpoints.manage.FinanceAgreementsEndpoint import FinanceAgreementsEndpoint
from pywise.endpoints.manage.FinanceBatchSetupsEndpoint import FinanceBatchSetupsEndpoint
from pywise.endpoints.manage.FinanceBillingCyclesEndpoint import FinanceBillingCyclesEndpoint
from pywise.endpoints.manage.FinanceBillingSetupsEndpoint import FinanceBillingSetupsEndpoint
from pywise.endpoints.manage.FinanceBillingStatusesEndpoint import FinanceBillingStatusesEndpoint
from pywise.endpoints.manage.FinanceBillingTermsEndpoint import FinanceBillingTermsEndpoint
from pywise.endpoints.manage.FinanceCurrenciesEndpoint import FinanceCurrenciesEndpoint
from pywise.endpoints.manage.FinanceDeliveryMethodsEndpoint import FinanceDeliveryMethodsEndpoint
from pywise.endpoints.manage.FinanceGlAccountsEndpoint import FinanceGlAccountsEndpoint
from pywise.endpoints.manage.FinanceGlCaptionsEndpoint import FinanceGlCaptionsEndpoint
from pywise.endpoints.manage.FinanceGlpathsEndpoint import FinanceGlpathsEndpoint
from pywise.endpoints.manage.FinanceInvoiceEmailTemplatesEndpoint import FinanceInvoiceEmailTemplatesEndpoint
from pywise.endpoints.manage.FinanceInvoicesEndpoint import FinanceInvoicesEndpoint
from pywise.endpoints.manage.FinanceInvoiceTemplatesEndpoint import FinanceInvoiceTemplatesEndpoint
from pywise.endpoints.manage.FinanceInvoiceTemplateSetupsEndpoint import FinanceInvoiceTemplateSetupsEndpoint
from pywise.endpoints.manage.FinanceTaxCodesEndpoint import FinanceTaxCodesEndpoint
from pywise.endpoints.manage.FinanceTaxIntegrationsEndpoint import FinanceTaxIntegrationsEndpoint

class FinanceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "finance")
        
        self.accountingPackages = self.register_child_endpoint(
            FinanceAccountingPackagesEndpoint(client, parent_endpoint=self)
        )
        self.accountingPackageSetup = self.register_child_endpoint(
            FinanceAccountingPackageSetupEndpoint(client, parent_endpoint=self)
        )
        self.agreements = self.register_child_endpoint(
            FinanceAgreementsEndpoint(client, parent_endpoint=self)
        )
        self.batchSetups = self.register_child_endpoint(
            FinanceBatchSetupsEndpoint(client, parent_endpoint=self)
        )
        self.billingCycles = self.register_child_endpoint(
            FinanceBillingCyclesEndpoint(client, parent_endpoint=self)
        )
        self.billingSetups = self.register_child_endpoint(
            FinanceBillingSetupsEndpoint(client, parent_endpoint=self)
        )
        self.billingStatuses = self.register_child_endpoint(
            FinanceBillingStatusesEndpoint(client, parent_endpoint=self)
        )
        self.billingTerms = self.register_child_endpoint(
            FinanceBillingTermsEndpoint(client, parent_endpoint=self)
        )
        self.currencies = self.register_child_endpoint(
            FinanceCurrenciesEndpoint(client, parent_endpoint=self)
        )
        self.deliveryMethods = self.register_child_endpoint(
            FinanceDeliveryMethodsEndpoint(client, parent_endpoint=self)
        )
        self.glAccounts = self.register_child_endpoint(
            FinanceGlAccountsEndpoint(client, parent_endpoint=self)
        )
        self.glCaptions = self.register_child_endpoint(
            FinanceGlCaptionsEndpoint(client, parent_endpoint=self)
        )
        self.glpaths = self.register_child_endpoint(
            FinanceGlpathsEndpoint(client, parent_endpoint=self)
        )
        self.invoiceEmailTemplates = self.register_child_endpoint(
            FinanceInvoiceEmailTemplatesEndpoint(client, parent_endpoint=self)
        )
        self.invoices = self.register_child_endpoint(
            FinanceInvoicesEndpoint(client, parent_endpoint=self)
        )
        self.invoiceTemplates = self.register_child_endpoint(
            FinanceInvoiceTemplatesEndpoint(client, parent_endpoint=self)
        )
        self.invoiceTemplateSetups = self.register_child_endpoint(
            FinanceInvoiceTemplateSetupsEndpoint(client, parent_endpoint=self)
        )
        self.taxCodes = self.register_child_endpoint(
            FinanceTaxCodesEndpoint(client, parent_endpoint=self)
        )
        self.taxIntegrations = self.register_child_endpoint(
            FinanceTaxIntegrationsEndpoint(client, parent_endpoint=self)
        )