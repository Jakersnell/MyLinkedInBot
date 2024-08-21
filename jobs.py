from enum import Enum
from typing import Set

class SearchSortBy(Enum):
    MOST_RECENT = "most-recent"
    MOST_RELEVANT = "most-relevant"

class JobDatePosted(Enum):
    ANY_TIME = "any-time"
    PAST_WEEK = "past-week"
    PAST_MONTH = "past-month"
    PAST_24_HOURS = "past-24-hours"

class JobExperienceLevel(Enum):
    INTERNSHIP = "internship"
    ENTRY_LEVEL = "entry-level"
    ASSOCIATE = "associate"
    MID_SENIOR_LEVEL = "mid-senior-level"
    DIRECTOR = "director"
    EXECUTIVE = "executive"

class JobType(Enum):
    FULL_TIME = "full-time"
    PART_TIME = "part-time"
    CONTRACT = "contract"
    TEMPORARY = "temporary"
    VOLUNTEER = "volunteer"
    INTERNSHIP = "internship"
    OTHER = "other"

class JobLocationType(Enum):
    ON_SITE = "on-site"
    HYBRID = "hybrid"
    REMOTE = "remote"

class JobRequiredEducation(Enum):
    UNKNOWN = "unknown"
    HIGH_SCHOOL = "high-school"
    ASSOCIATES = "associates"
    BACHELORS = "bachelors"
    MASTERS = "masters"
    PHD = "phd"

class Job:
    company_name: str
    location: str
    location_type: JobLocationType
    job_experience_level: JobExperienceLevel
    job_age: str # this should be a different type
    starting_yearly: int
    skills: Set[str]
    required_education: JobRequiredEducation
    description: str

    def __init__(self,
        company_name: str,
        location: str,
        location_type: JobLocationType,
        job_experience_level: JobExperienceLevel,
        job_age: str,
        starting_yearly: int,
        skills: Set[str],
        required_education: JobRequiredEducation,
        description: str
    ):
        self.company_name = company_name
        self.location = location
        self.location_type = location_type
        self.job_experience_level = job_experience_level
        self.job_age = job_age
        self.starting_yearly = starting_yearly
        self.skills = skills
        self.required_education = required_education
        self.description = description