from dataclasses import dataclass
from typing import Optional, List

@dataclass
class User:
    id: str
    name: str
    age: int
    weight: float
    height: float
    goals: List[str]
    activity_level: str
    health_conditions: Optional[List[str]] = None
    dietary_restrictions: Optional[List[str]] = None
