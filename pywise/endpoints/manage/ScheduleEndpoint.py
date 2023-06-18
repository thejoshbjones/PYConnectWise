from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.endpoints.manage.ScheduleCalendarsEndpoint import ScheduleCalendarsEndpoint
from pywise.endpoints.manage.ScheduleColorsEndpoint import ScheduleColorsEndpoint
from pywise.endpoints.manage.ScheduleDetailsEndpoint import ScheduleDetailsEndpoint
from pywise.endpoints.manage.ScheduleEntriesEndpoint import ScheduleEntriesEndpoint
from pywise.endpoints.manage.ScheduleHolidayListsEndpoint import ScheduleHolidayListsEndpoint
from pywise.endpoints.manage.SchedulePortalcalendarsEndpoint import SchedulePortalcalendarsEndpoint
from pywise.endpoints.manage.ScheduleReminderTimesEndpoint import ScheduleReminderTimesEndpoint
from pywise.endpoints.manage.ScheduleStatusesEndpoint import ScheduleStatusesEndpoint
from pywise.endpoints.manage.ScheduleTypesEndpoint import ScheduleTypesEndpoint

class ScheduleEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "schedule")
        
        self.calendars = self.register_child_endpoint(
            ScheduleCalendarsEndpoint(client, parent_endpoint=self)
        )
        self.colors = self.register_child_endpoint(
            ScheduleColorsEndpoint(client, parent_endpoint=self)
        )
        self.details = self.register_child_endpoint(
            ScheduleDetailsEndpoint(client, parent_endpoint=self)
        )
        self.entries = self.register_child_endpoint(
            ScheduleEntriesEndpoint(client, parent_endpoint=self)
        )
        self.holidayLists = self.register_child_endpoint(
            ScheduleHolidayListsEndpoint(client, parent_endpoint=self)
        )
        self.portalcalendars = self.register_child_endpoint(
            SchedulePortalcalendarsEndpoint(client, parent_endpoint=self)
        )
        self.reminderTimes = self.register_child_endpoint(
            ScheduleReminderTimesEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            ScheduleStatusesEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            ScheduleTypesEndpoint(client, parent_endpoint=self)
        )