"""Models used to identify and enforce types in the API"""
from enum import Enum

from pydantic import BaseModel, conint


class Coverage(BaseModel):
    """Model for a member's coverage where values must be positive integers"""
    deductible: conint(ge=0)
    stop_loss: conint(ge=0)
    oop_max: conint(ge=0)


class Strategy(Enum):
    """Enum of available strategies"""
    average = "average"
    minimum = "minimum"
    maximum = "maximum"
