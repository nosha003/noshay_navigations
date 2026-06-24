"""Tests for data models."""

import unittest
from datetime import datetime, date
from run_coaching.models import Runner, TrainingSession, TrainingPlan


class TestRunner(unittest.TestCase):
    """Test the Runner model."""
    
    def test_runner_creation(self):
        """Test creating a runner."""
        runner = Runner(
            id="runner_1",
            name="John Doe",
            email="john@example.com",
            age=30,
            experience_level="intermediate"
        )
        
        self.assertEqual(runner.id, "runner_1")
        self.assertEqual(runner.name, "John Doe")
        self.assertEqual(runner.email, "john@example.com")
        self.assertEqual(runner.age, 30)
        self.assertEqual(runner.experience_level, "intermediate")
        self.assertIsInstance(runner.created_at, datetime)
    
    def test_runner_str(self):
        """Test runner string representation."""
        runner = Runner(
            id="runner_1",
            name="John Doe",
            email="john@example.com",
            age=30,
            experience_level="intermediate"
        )
        
        self.assertIn("runner_1", str(runner))
        self.assertIn("John Doe", str(runner))


class TestTrainingSession(unittest.TestCase):
    """Test the TrainingSession model."""
    
    def test_session_creation(self):
        """Test creating a training session."""
        session = TrainingSession(
            id="session_1",
            runner_id="runner_1",
            date=date(2024, 1, 15),
            distance_km=5.0,
            duration_minutes=30,
            session_type="easy"
        )
        
        self.assertEqual(session.id, "session_1")
        self.assertEqual(session.runner_id, "runner_1")
        self.assertEqual(session.distance_km, 5.0)
        self.assertEqual(session.duration_minutes, 30)
        self.assertEqual(session.session_type, "easy")
    
    def test_pace_calculation(self):
        """Test automatic pace calculation."""
        session = TrainingSession(
            id="session_1",
            runner_id="runner_1",
            date=date(2024, 1, 15),
            distance_km=5.0,
            duration_minutes=30
        )
        
        # 30 minutes / 5 km = 6 min/km
        self.assertEqual(session.pace_min_per_km, 6.0)
    
    def test_pace_with_manual_value(self):
        """Test that manual pace value is preserved."""
        session = TrainingSession(
            id="session_1",
            runner_id="runner_1",
            date=date(2024, 1, 15),
            distance_km=5.0,
            duration_minutes=30,
            pace_min_per_km=5.5
        )
        
        self.assertEqual(session.pace_min_per_km, 5.5)


class TestTrainingPlan(unittest.TestCase):
    """Test the TrainingPlan model."""
    
    def test_plan_creation(self):
        """Test creating a training plan."""
        plan = TrainingPlan(
            id="plan_1",
            runner_id="runner_1",
            name="5K Training Plan",
            start_date=date(2024, 1, 1),
            end_date=date(2024, 3, 1),
            goal="Complete 5K in under 25 minutes",
            weekly_mileage_target=20.0
        )
        
        self.assertEqual(plan.id, "plan_1")
        self.assertEqual(plan.runner_id, "runner_1")
        self.assertEqual(plan.name, "5K Training Plan")
        self.assertEqual(plan.goal, "Complete 5K in under 25 minutes")
        self.assertEqual(plan.weekly_mileage_target, 20.0)


if __name__ == "__main__":
    unittest.main()
