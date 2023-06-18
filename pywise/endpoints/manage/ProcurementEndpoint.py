from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.endpoints.manage.ProcurementAdjustmentsEndpoint import ProcurementAdjustmentsEndpoint
from pywise.endpoints.manage.ProcurementCatalogEndpoint import ProcurementCatalogEndpoint
from pywise.endpoints.manage.ProcurementCategoriesEndpoint import ProcurementCategoriesEndpoint
from pywise.endpoints.manage.ProcurementManufacturersEndpoint import ProcurementManufacturersEndpoint
from pywise.endpoints.manage.ProcurementOnhandserialnumbersEndpoint import ProcurementOnhandserialnumbersEndpoint
from pywise.endpoints.manage.ProcurementPricingschedulesEndpoint import ProcurementPricingschedulesEndpoint
from pywise.endpoints.manage.ProcurementProductsEndpoint import ProcurementProductsEndpoint
from pywise.endpoints.manage.ProcurementPurchaseordersEndpoint import ProcurementPurchaseordersEndpoint
from pywise.endpoints.manage.ProcurementPurchaseorderstatusesEndpoint import ProcurementPurchaseorderstatusesEndpoint
from pywise.endpoints.manage.ProcurementPurchasingDemandsEndpoint import ProcurementPurchasingDemandsEndpoint
from pywise.endpoints.manage.ProcurementRmaActionsEndpoint import ProcurementRmaActionsEndpoint
from pywise.endpoints.manage.ProcurementRMADispositionsEndpoint import ProcurementRMADispositionsEndpoint
from pywise.endpoints.manage.ProcurementRmaStatusesEndpoint import ProcurementRmaStatusesEndpoint
from pywise.endpoints.manage.ProcurementRmaTagsEndpoint import ProcurementRmaTagsEndpoint
from pywise.endpoints.manage.ProcurementSettingsEndpoint import ProcurementSettingsEndpoint
from pywise.endpoints.manage.ProcurementShipmentmethodsEndpoint import ProcurementShipmentmethodsEndpoint
from pywise.endpoints.manage.ProcurementTypesEndpoint import ProcurementTypesEndpoint
from pywise.endpoints.manage.ProcurementUnitOfMeasuresEndpoint import ProcurementUnitOfMeasuresEndpoint
from pywise.endpoints.manage.ProcurementWarehouseBinsEndpoint import ProcurementWarehouseBinsEndpoint
from pywise.endpoints.manage.ProcurementWarehousesEndpoint import ProcurementWarehousesEndpoint

class ProcurementEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "procurement")
        
        self.adjustments = self.register_child_endpoint(
            ProcurementAdjustmentsEndpoint(client, parent_endpoint=self)
        )
        self.catalog = self.register_child_endpoint(
            ProcurementCatalogEndpoint(client, parent_endpoint=self)
        )
        self.categories = self.register_child_endpoint(
            ProcurementCategoriesEndpoint(client, parent_endpoint=self)
        )
        self.manufacturers = self.register_child_endpoint(
            ProcurementManufacturersEndpoint(client, parent_endpoint=self)
        )
        self.onhandserialnumbers = self.register_child_endpoint(
            ProcurementOnhandserialnumbersEndpoint(client, parent_endpoint=self)
        )
        self.pricingschedules = self.register_child_endpoint(
            ProcurementPricingschedulesEndpoint(client, parent_endpoint=self)
        )
        self.products = self.register_child_endpoint(
            ProcurementProductsEndpoint(client, parent_endpoint=self)
        )
        self.purchaseorders = self.register_child_endpoint(
            ProcurementPurchaseordersEndpoint(client, parent_endpoint=self)
        )
        self.purchaseorderstatuses = self.register_child_endpoint(
            ProcurementPurchaseorderstatusesEndpoint(client, parent_endpoint=self)
        )
        self.purchasingDemands = self.register_child_endpoint(
            ProcurementPurchasingDemandsEndpoint(client, parent_endpoint=self)
        )
        self.rmaActions = self.register_child_endpoint(
            ProcurementRmaActionsEndpoint(client, parent_endpoint=self)
        )
        self.RMADispositions = self.register_child_endpoint(
            ProcurementRMADispositionsEndpoint(client, parent_endpoint=self)
        )
        self.rmaStatuses = self.register_child_endpoint(
            ProcurementRmaStatusesEndpoint(client, parent_endpoint=self)
        )
        self.rmaTags = self.register_child_endpoint(
            ProcurementRmaTagsEndpoint(client, parent_endpoint=self)
        )
        self.settings = self.register_child_endpoint(
            ProcurementSettingsEndpoint(client, parent_endpoint=self)
        )
        self.shipmentmethods = self.register_child_endpoint(
            ProcurementShipmentmethodsEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            ProcurementTypesEndpoint(client, parent_endpoint=self)
        )
        self.unitOfMeasures = self.register_child_endpoint(
            ProcurementUnitOfMeasuresEndpoint(client, parent_endpoint=self)
        )
        self.warehouseBins = self.register_child_endpoint(
            ProcurementWarehouseBinsEndpoint(client, parent_endpoint=self)
        )
        self.warehouses = self.register_child_endpoint(
            ProcurementWarehousesEndpoint(client, parent_endpoint=self)
        )