"""Data models for run coaching application."""

from datetime import datetime, date
from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class Runner:
    """Represents a runner/athlete in the coaching program."""
    
    id: str
    name: str
    email: str
    age: int
    experience_level: str  # beginner, intermediate, advanced
    created_at: datetime = field(default_factory=datetime.now)
    
    def __str__(self):
        return f"Runner({self.id}, {self.name}, {self.experience_level})"


@dataclass
class TrainingSession:
    """Represents a single training session/run."""
    
    id: str
    runner_id: str
    date: date
    distance_km: float
    duration_minutes: int
    pace_min_per_km: Optional[float] = None
    notes: str = ""
    session_type: str = "easy"  # easy, tempo, interval, long, recovery
    
    def __post_init__(self):
        """Calculate pace if not provided."""
        if self.pace_min_per_km is None and self.duration_minutes > 0 and self.distance_km > 0:
            self.pace_min_per_km = self.duration_minutes / self.distance_km
    
    def __str__(self):
        return f"Session({self.date}, {self.distance_km}km, {self.session_type})"


@dataclass
class TrainingPlan:
    """Represents a training plan for a runner."""
    
    id: str
    runner_id: str
    name: str
    start_date: date
    end_date: date
    goal: str  # e.g., "Complete 5K", "Marathon sub-4:00"
    weekly_mileage_target: float
    description: str = ""
    
    def __str__(self):
        return f"TrainingPlan({self.name}, {self.goal})"
