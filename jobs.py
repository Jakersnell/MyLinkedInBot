from enum import Enum
from typing import Set

class SearchSortBy(Enum):
    MOST_RECENT = 1
    MOST_RELEVANT = 2

class JobDatePosted(Enum):
    ANY_TIME = 1
    PAST_WEEK = 2
    PAST_MONTH = 3
    PAST_24_HOURS = 4

class JobExperienceLevel(Enum):
    INTERNSHIP = 1
    ENTRY_LEVEL = 2
    ASSOCIATE = 3
    MID_SENIOR_LEVEL = 4
    DIRECTOR = 5
    EXECUTIVE = 6

class JobType(Enum):
    FULL_TIME = 1
    PART_TIME = 2
    CONTRACT = 3
    TEMPORARY = 4
    VOLUNTEER = 5
    INTERNSHIP = 6
    OTHER = 7

class JobLocationType(Enum):
    ON_SITE = 1
    HYBRID = 2
    REMOTE = 3

class JobRequiredEducation(Enum):
    UNKNOWN = 0
    HIGH_SCHOOL = 1
    ASSOCIATES = 2
    BACHELORS = 3
    MASTERS = 4
    PHD = 5

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