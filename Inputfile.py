from pydantic import BaseModel,Field
from typing import Optional,List


class StudentInput(BaseModel):
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    math_score: float
    reading_score: float
    writing_score: float
