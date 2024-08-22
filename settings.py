from dataclasses import dataclass
from typing import List, Set, Any, Dict
from jobs import SearchSortBy, JobDatePosted, JobExperienceLevel, JobType, JobLocationType


@dataclass
class LoginSettings:
    email: str
    password: str

@dataclass
class LinkedInSearchSettings:
    sort_by: SearchSortBy
    date_posted: JobDatePosted
    queries: List[str]
    experience_levels: Set[JobExperienceLevel]
    job_types: Set[JobType]
    location_types: Set[JobLocationType]

@dataclass
class JobFilterSettings:
    job_experience_level: JobExperienceLevel
    job_age: str
    starting_yearly: int
    skills: List[str]
    excluded_keywords: List[str]
    exclude_companies: List[str]

@dataclass
class AiFilterSettings:
    prompts: List[List[str]]

@dataclass
class GlobalBotSettings:
    open_ai_api_key: str
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
    sort_by = SearchSortBy(search_settings['sort_by'])
    date_posted = search_settings['date_posted']
    queries = search_settings['queries']
    experience_levels = {JobExperienceLevel(experience_level) for experience_level in search_settings['experience_levels']}
    job_types = {JobType(job_type) for job_type in search_settings['job_types']}
    location_types = {JobLocationType(location_type) for location_type in search_settings['location_types']}
    return LinkedInSearchSettings(sort_by, date_posted, queries, experience_levels, job_types, location_types)

def _build_job_filter_settings(job_filter_settings: Dict[str, Any]) -> JobFilterSettings:
    pass
