"""Tests for storage layer."""

import unittest
import os
import tempfile
import shutil
from datetime import date, datetime
from run_coaching.models import Runner, TrainingSession, TrainingPlan
from run_coaching.storage import Storage


class TestStorage(unittest.TestCase):
    """Test the Storage class."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary directory for test data
        self.test_dir = tempfile.mkdtemp()
        self.storage = Storage(data_dir=self.test_dir)
    
    def tearDown(self):
        """Clean up test fixtures."""
        # Remove the temporary directory
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_save_and_get_runner(self):
        """Test saving and retrieving a runner."""
        runner = Runner(
            id="runner_1",
            name="Jane Smith",
            email="jane@example.com",
            age=28,
            experience_level="advanced"
        )
        
        self.storage.save_runner(runner)
        retrieved = self.storage.get_runner_by_id("runner_1")
        
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.id, runner.id)
        self.assertEqual(retrieved.name, runner.name)
        self.assertEqual(retrieved.email, runner.email)
        self.assertEqual(retrieved.age, runner.age)
        self.assertEqual(retrieved.experience_level, runner.experience_level)
    
    def test_get_all_runners(self):
        """Test getting all runners."""
        runner1 = Runner("r1", "Alice", "alice@example.com", 25, "beginner")
        runner2 = Runner("r2", "Bob", "bob@example.com", 30, "intermediate")
        
        self.storage.save_runner(runner1)
        self.storage.save_runner(runner2)
        
        all_runners = self.storage.get_all_runners()
        self.assertEqual(len(all_runners), 2)
    
    def test_update_runner(self):
        """Test updating an existing runner."""
        runner = Runner("r1", "Charlie", "charlie@example.com", 35, "beginner")
        self.storage.save_runner(runner)
        
        # Update the runner
        runner.experience_level = "intermediate"
        self.storage.save_runner(runner)
        
        retrieved = self.storage.get_runner_by_id("r1")
        self.assertEqual(retrieved.experience_level, "intermediate")
    
    def test_save_and_get_session(self):
        """Test saving and retrieving training sessions."""
        runner = Runner("r1", "Dave", "dave@example.com", 40, "advanced")
        self.storage.save_runner(runner)
        
        session = TrainingSession(
            id="s1",
            runner_id="r1",
            date=date(2024, 1, 15),
            distance_km=10.0,
            duration_minutes=60,
            session_type="long"
        )
        
        self.storage.save_session(session)
        sessions = self.storage.get_sessions_for_runner("r1")
        
        self.assertEqual(len(sessions), 1)
        self.assertEqual(sessions[0].id, "s1")
        self.assertEqual(sessions[0].distance_km, 10.0)
    
    def test_multiple_sessions(self):
        """Test storing multiple sessions for a runner."""
        runner = Runner("r1", "Eve", "eve@example.com", 32, "intermediate")
        self.storage.save_runner(runner)
        
        session1 = TrainingSession("s1", "r1", date(2024, 1, 15), 5.0, 30)
        session2 = TrainingSession("s2", "r1", date(2024, 1, 16), 7.0, 42)
        
        self.storage.save_session(session1)
        self.storage.save_session(session2)
        
        sessions = self.storage.get_sessions_for_runner("r1")
        self.assertEqual(len(sessions), 2)
    
    def test_save_and_get_plan(self):
        """Test saving and retrieving training plans."""
        runner = Runner("r1", "Frank", "frank@example.com", 28, "beginner")
        self.storage.save_runner(runner)
        
        plan = TrainingPlan(
            id="p1",
            runner_id="r1",
            name="Couch to 5K",
            start_date=date(2024, 1, 1),
            end_date=date(2024, 3, 1),
            goal="Complete 5K",
            weekly_mileage_target=15.0
        )
        
        self.storage.save_plan(plan)
        plans = self.storage.get_plans_for_runner("r1")
        
        self.assertEqual(len(plans), 1)
        self.assertEqual(plans[0].id, "p1")
        self.assertEqual(plans[0].name, "Couch to 5K")
        self.assertEqual(plans[0].weekly_mileage_target, 15.0)
    
    def test_nonexistent_runner(self):
        """Test getting a non-existent runner."""
        retrieved = self.storage.get_runner_by_id("nonexistent")
        self.assertIsNone(retrieved)
    
    def test_sessions_sorted_by_date(self):
        """Test that sessions are returned sorted by date (newest first)."""
        runner = Runner("r1", "Grace", "grace@example.com", 27, "advanced")
        self.storage.save_runner(runner)
        
        session1 = TrainingSession("s1", "r1", date(2024, 1, 10), 5.0, 30)
        session2 = TrainingSession("s2", "r1", date(2024, 1, 15), 6.0, 36)
        session3 = TrainingSession("s3", "r1", date(2024, 1, 12), 5.5, 33)
        
        self.storage.save_session(session1)
        self.storage.save_session(session2)
        self.storage.save_session(session3)
        
        sessions = self.storage.get_sessions_for_runner("r1")
        
        # Should be sorted newest first
        self.assertEqual(sessions[0].date, date(2024, 1, 15))
        self.assertEqual(sessions[1].date, date(2024, 1, 12))
        self.assertEqual(sessions[2].date, date(2024, 1, 10))


if __name__ == "__main__":
    unittest.main()
