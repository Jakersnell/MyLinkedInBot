from dataclasses import dataclass
from typing import List, Set, Any, Dict
from jobs import SearchSortBy, JobDatePosted, JobExperienceLevel, JobType, JobLocationType


@dataclass
class LoginSettings:
    email: str
    password: str

@dataclass
class LinkedInSearchSettings:
    sort_by: SearchSortBy | None
    date_posted: JobDatePosted | None
    queries: List[str]
    experience_levels: Set[JobExperienceLevel]
    job_types: Set[JobType]
    location_types: Set[JobLocationType]

@dataclass
class JobFilterSettings:
    job_experience_level: JobExperienceLevel | None
    job_age: str | None
    starting_yearly: int | None
    skills: List[str]
    excluded_keywords: List[str]
    exclude_companies: List[str]

@dataclass
class AiFilterSettings:
    prompts: List[List[str]]

@dataclass
class GlobalBotSettings:
    login_settings: LoginSettings
    linkedin_search_settings: LinkedInSearchSettings
    job_filter_settings: JobFilterSettings

def build_settings(raw_settings: Dict[str, Any]) -> GlobalBotSettings:
    pass

def _build_login_settings(raw_settings: Dict[str, Any]) -> LoginSettings:
    email = raw_settings['email']
    password = raw_settings['password']
    return LoginSettings(email, password)

def _build_linkedin_search_settings(search_settings: Dict[str, Any]) -> LinkedInSearchSettings:
    sort_by = search_settings['sort_by']
    date_posted = search_settings['date_posted']
    queries = search_settings['queries']
    experience_levels = search_settings['experience_levels']
    job_types = search_settings['job_types']
    location_types = search_settings['location_types']
