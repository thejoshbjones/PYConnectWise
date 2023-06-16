from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementUnitOfMeasuresIdConversionsIdEndpoint import ProcurementUnitOfMeasuresIdConversionsIdEndpoint
from pywise.endpoints.ProcurementUnitOfMeasuresIdConversionsCountEndpoint import ProcurementUnitOfMeasuresIdConversionsCountEndpoint
from pywise.models.ConversionModel import ConversionModel

class ProcurementUnitOfMeasuresIdConversionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "conversions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementUnitOfMeasuresIdConversionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementUnitOfMeasuresIdConversionsIdEndpoint:
        child = ProcurementUnitOfMeasuresIdConversionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ConversionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ConversionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ConversionModel]:
        return self._parse_many(ConversionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ConversionModel:
        return self._parse_one(ConversionModel, super().make_request("POST", params=params))
        