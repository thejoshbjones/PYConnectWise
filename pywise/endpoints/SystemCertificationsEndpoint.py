from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemCertificationsIdEndpoint import SystemCertificationsIdEndpoint
from pywise.endpoints.SystemCertificationsCountEndpoint import SystemCertificationsCountEndpoint
from pywise.models.CertificationModel import CertificationModel

class SystemCertificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "certifications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemCertificationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemCertificationsIdEndpoint:
        child = SystemCertificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CertificationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CertificationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CertificationModel]:
        return self._parse_many(CertificationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CertificationModel:
        return self._parse_one(CertificationModel, super().make_request("POST", params=params))
        