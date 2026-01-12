"""Storage layer for run coaching application using JSON files."""

import json
import os
from datetime import datetime, date
from typing import List, Optional, Dict, Any
from run_coaching.models import Runner, TrainingSession, TrainingPlan


class Storage:
    """Simple JSON-based storage for the application."""
    
    def __init__(self, data_dir: str = "data"):
        """Initialize storage with a data directory."""
        self.data_dir = data_dir
        self._ensure_data_dir()
        
    def _ensure_data_dir(self):
        """Create data directory if it doesn't exist."""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def _get_file_path(self, entity_type: str) -> str:
        """Get the file path for an entity type."""
        return os.path.join(self.data_dir, f"{entity_type}.json")
    
    def _serialize_date(self, obj: Any) -> Any:
        """Serialize datetime and date objects to ISO format."""
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, date):
            return obj.isoformat()
        return obj
    
    def _load_data(self, entity_type: str) -> List[Dict]:
        """Load data from JSON file."""
        file_path = self._get_file_path(entity_type)
        if not os.path.exists(file_path):
            return []
        
        with open(file_path, 'r') as f:
            return json.load(f)
    
    def _save_data(self, entity_type: str, data: List[Dict]):
        """Save data to JSON file."""
        file_path = self._get_file_path(entity_type)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, default=self._serialize_date)
    
    # Runner operations
    def save_runner(self, runner: Runner):
        """Save a runner to storage."""
        runners = self._load_data("runners")
        runner_dict = {
            "id": runner.id,
            "name": runner.name,
            "email": runner.email,
            "age": runner.age,
            "experience_level": runner.experience_level,
            "created_at": runner.created_at.isoformat()
        }
        
        # Update if exists, otherwise append
        updated = False
        for i, r in enumerate(runners):
            if r["id"] == runner.id:
                runners[i] = runner_dict
                updated = True
                break
        
        if not updated:
            runners.append(runner_dict)
        
        self._save_data("runners", runners)
    
    def get_all_runners(self) -> List[Runner]:
        """Get all runners from storage."""
        runners_data = self._load_data("runners")
        runners = []
        for r in runners_data:
            runners.append(Runner(
                id=r["id"],
                name=r["name"],
                email=r["email"],
                age=r["age"],
                experience_level=r["experience_level"],
                created_at=datetime.fromisoformat(r["created_at"])
            ))
        return runners
    
    def get_runner_by_id(self, runner_id: str) -> Optional[Runner]:
        """Get a runner by ID."""
        runners = self.get_all_runners()
        for runner in runners:
            if runner.id == runner_id:
                return runner
        return None
    
    # Training Session operations
    def save_session(self, session: TrainingSession):
        """Save a training session to storage."""
        sessions = self._load_data("sessions")
        session_dict = {
            "id": session.id,
            "runner_id": session.runner_id,
            "date": session.date.isoformat(),
            "distance_km": session.distance_km,
            "duration_minutes": session.duration_minutes,
            "pace_min_per_km": session.pace_min_per_km,
            "notes": session.notes,
            "session_type": session.session_type
        }
        
        # Update if exists, otherwise append
        updated = False
        for i, s in enumerate(sessions):
            if s["id"] == session.id:
                sessions[i] = session_dict
                updated = True
                break
        
        if not updated:
            sessions.append(session_dict)
        
        self._save_data("sessions", sessions)
    
    def get_sessions_for_runner(self, runner_id: str) -> List[TrainingSession]:
        """Get all training sessions for a runner."""
        sessions_data = self._load_data("sessions")
        sessions = []
        for s in sessions_data:
            if s["runner_id"] == runner_id:
                sessions.append(TrainingSession(
                    id=s["id"],
                    runner_id=s["runner_id"],
                    date=date.fromisoformat(s["date"]),
                    distance_km=s["distance_km"],
                    duration_minutes=s["duration_minutes"],
                    pace_min_per_km=s.get("pace_min_per_km"),
                    notes=s.get("notes", ""),
                    session_type=s.get("session_type", "easy")
                ))
        return sorted(sessions, key=lambda x: x.date, reverse=True)
    
    # Training Plan operations
    def save_plan(self, plan: TrainingPlan):
        """Save a training plan to storage."""
        plans = self._load_data("plans")
        plan_dict = {
            "id": plan.id,
            "runner_id": plan.runner_id,
            "name": plan.name,
            "start_date": plan.start_date.isoformat(),
            "end_date": plan.end_date.isoformat(),
            "goal": plan.goal,
            "weekly_mileage_target": plan.weekly_mileage_target,
            "description": plan.description
        }
        
        # Update if exists, otherwise append
        updated = False
        for i, p in enumerate(plans):
            if p["id"] == plan.id:
                plans[i] = plan_dict
                updated = True
                break
        
        if not updated:
            plans.append(plan_dict)
        
        self._save_data("plans", plans)
    
    def get_plans_for_runner(self, runner_id: str) -> List[TrainingPlan]:
        """Get all training plans for a runner."""
        plans_data = self._load_data("plans")
        plans = []
        for p in plans_data:
            if p["runner_id"] == runner_id:
                plans.append(TrainingPlan(
                    id=p["id"],
                    runner_id=p["runner_id"],
                    name=p["name"],
                    start_date=date.fromisoformat(p["start_date"]),
                    end_date=date.fromisoformat(p["end_date"]),
                    goal=p["goal"],
                    weekly_mileage_target=p["weekly_mileage_target"],
                    description=p.get("description", "")
                ))
        return plans
