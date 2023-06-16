import os
import base64
import requests
from pywise.endpoints.CompanyEndpoint import CompanyEndpoint
from pywise.endpoints.ConfigurationsEndpoint import ConfigurationsEndpoint
from pywise.endpoints.ExpenseEndpoint import ExpenseEndpoint
from pywise.endpoints.FinanceEndpoint import FinanceEndpoint
from pywise.endpoints.MarketingEndpoint import MarketingEndpoint
from pywise.endpoints.ProcurementEndpoint import ProcurementEndpoint
from pywise.endpoints.ProjectEndpoint import ProjectEndpoint
from pywise.endpoints.SalesEndpoint import SalesEndpoint
from pywise.endpoints.ScheduleEndpoint import ScheduleEndpoint
from pywise.endpoints.ServiceEndpoint import ServiceEndpoint
from pywise.endpoints.SystemEndpoint import SystemEndpoint
from pywise.endpoints.TimeEndpoint import TimeEndpoint


class ConnectWiseManageAPIClient:
    def __init__(
        self,
        company_name,
        company_url,
        client_id,
        public_key,
        private_key,
        codebase=None,
    ):
        self.client_id = client_id
        self.company_name = company_name
        self.company_url = company_url
        self.public_key = public_key
        self.private_key = private_key
        self.codebase = codebase

        if not codebase:
            self.codebase = self.__try_get_codebase_from_api(
                company_url=company_url,
                company_name=company_name,
                headers=self.get_headers(),
            )

        ## ENDPOINT REGISTRATION BELOW ##
        self.company = CompanyEndpoint(self)
        self.configurations = ConfigurationsEndpoint(self)
        self.expense = ExpenseEndpoint(self)
        self.finance = FinanceEndpoint(self)
        self.marketing = MarketingEndpoint(self)
        self.procurement = ProcurementEndpoint(self)
        self.project = ProjectEndpoint(self)
        self.sales = SalesEndpoint(self)
        self.schedule = ScheduleEndpoint(self)
        self.service = ServiceEndpoint(self)
        self.system = SystemEndpoint(self)
        self.time = TimeEndpoint(self)

    def get_url(self):
        return f"https://{self.company_url}/{self.codebase.strip('/')}/apis/3.0"

    def __try_get_codebase_from_api(self, company_url, company_name, headers):
        result = ""
        try:
            url = f"https://{company_url}/login/companyinfo/{company_name}"
            result = (
                requests.request("GET", url, headers=headers).json().get("Codebase")
            )
        except:
            result = None
        return result

    def __get_auth_string(self):
        return "Basic " + base64.b64encode(
            bytes(
                f"{self.company_name}+{self.public_key}:{self.private_key}",
                encoding="utf8",
            )
        ).decode("ascii")

    def get_headers(self):
        headers = {
            "Content-Type": "application/json",
            "clientId": self.client_id,
            "Authorization": self.__get_auth_string(),
        }
        return headers
