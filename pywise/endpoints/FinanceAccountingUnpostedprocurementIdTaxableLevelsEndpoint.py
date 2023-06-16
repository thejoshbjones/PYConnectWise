from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAccountingUnpostedprocurementIdTaxableLevelsIdEndpoint import FinanceAccountingUnpostedprocurementIdTaxableLevelsIdEndpoint
from pywise.endpoints.FinanceAccountingUnpostedprocurementIdTaxableLevelsCountEndpoint import FinanceAccountingUnpostedprocurementIdTaxableLevelsCountEndpoint
from pywise.models.UnpostedProcurementTaxableLevelModel import UnpostedProcurementTaxableLevelModel

class FinanceAccountingUnpostedprocurementIdTaxableLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingUnpostedprocurementIdTaxableLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAccountingUnpostedprocurementIdTaxableLevelsIdEndpoint:
        child = FinanceAccountingUnpostedprocurementIdTaxableLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[UnpostedProcurementTaxableLevelModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            UnpostedProcurementTaxableLevelModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[UnpostedProcurementTaxableLevelModel]:
        return self._parse_many(UnpostedProcurementTaxableLevelModel, super().make_request("GET", params=params))
        