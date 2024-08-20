from selenium.webdriver.remote.webdriver import WebDriver
from logging import Logger
from typing import Set
from jobs import *


class JobSearchBot:
    browser: WebDriver
    logger: Logger

    query: str
    sort_by: SearchSortBy
    date_posted: JobDatePosted
    experience_levels: Set[JobExperienceLevel]
    job_types: Set[JobType]
    location_types: Set[JobLocationType]

    def __init__(self, browser: WebDriver, logger: Logger):
        self.browser = browser
        self.logger = logger

    def search(self,
               query: str,
               sort_by: SearchSortBy,
               date_posted: JobDatePosted,
               experience_levels: Set[JobExperienceLevel],
               job_types: Set[JobType],
               location_types: Set[JobLocationType]
               ) -> None:
        self.query = query
        self.sort_by = sort_by
        self.date_posted = date_posted
        self.experience_levels = experience_levels
        self.job_types = job_types
        self.location_types = location_types
        self._search_with_query()
        self._apply_search_filters()

    def _search_with_query(self) -> None:
        pass

    def _apply_search_filters(self) -> None:
        pass

    def get_page_jobs(self):
        pass