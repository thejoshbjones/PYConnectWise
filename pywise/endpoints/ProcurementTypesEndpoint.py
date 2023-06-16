from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementTypesIdEndpoint import ProcurementTypesIdEndpoint
from pywise.endpoints.ProcurementTypesCountEndpoint import ProcurementTypesCountEndpoint
from pywise.endpoints.ProcurementTypesInfoEndpoint import ProcurementTypesInfoEndpoint
from pywise.models.ProductTypeModel import ProductTypeModel

class ProcurementTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementTypesIdEndpoint:
        child = ProcurementTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProductTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProductTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProductTypeModel]:
        return self._parse_many(ProductTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProductTypeModel:
        return self._parse_one(ProductTypeModel, super().make_request("POST", params=params))
        