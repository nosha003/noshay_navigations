#!/usr/bin/env python3
"""Demo script to showcase the run coaching application."""

from datetime import date, datetime
from run_coaching.models import Runner, TrainingSession, TrainingPlan
from run_coaching.storage import Storage
from tabulate import tabulate

def demo():
    """Run a demo of the application."""
    print("="*60)
    print("Run Coaching Application - Demo")
    print("="*60)
    
    # Initialize storage
    storage = Storage(data_dir="demo_data")
    
    # 1. Create runners
    print("\n1. Creating runners...")
    runner1 = Runner(
        id="runner_001",
        name="Sarah Johnson",
        email="sarah.j@example.com",
        age=28,
        experience_level="intermediate"
    )
    
    runner2 = Runner(
        id="runner_002",
        name="Mike Chen",
        email="mike.c@example.com",
        age=35,
        experience_level="beginner"
    )
    
    storage.save_runner(runner1)
    storage.save_runner(runner2)
    print("✓ Runners created successfully")
    
    # 2. Display runners
    print("\n2. All Runners:")
    runners = storage.get_all_runners()
    runner_data = [[r.id, r.name, r.email, r.age, r.experience_level] for r in runners]
    print(tabulate(runner_data, headers=["ID", "Name", "Email", "Age", "Level"], tablefmt="grid"))
    
    # 3. Log training sessions for Sarah
    print("\n3. Logging training sessions for Sarah...")
    sessions = [
        TrainingSession("s001", "runner_001", date(2024, 1, 15), 5.0, 28, session_type="easy"),
        TrainingSession("s002", "runner_001", date(2024, 1, 17), 8.0, 52, session_type="tempo"),
        TrainingSession("s003", "runner_001", date(2024, 1, 19), 12.0, 84, session_type="long"),
        TrainingSession("s004", "runner_001", date(2024, 1, 21), 6.0, 36, session_type="interval"),
    ]
    
    for session in sessions:
        storage.save_session(session)
    print("✓ Training sessions logged")
    
    # 4. Display Sarah's training history
    print("\n4. Sarah's Training History:")
    sarah_sessions = storage.get_sessions_for_runner("runner_001")
    session_data = [
        [s.date, f"{s.distance_km:.1f}", s.duration_minutes, 
         f"{s.pace_min_per_km:.2f}", s.session_type]
        for s in sarah_sessions
    ]
    print(tabulate(session_data, 
                  headers=["Date", "Distance (km)", "Duration (min)", "Pace (min/km)", "Type"],
                  tablefmt="grid"))
    
    # 5. Create training plan for Mike
    print("\n5. Creating training plan for Mike...")
    plan = TrainingPlan(
        id="plan_001",
        runner_id="runner_002",
        name="Couch to 5K - 8 Week Plan",
        start_date=date(2024, 2, 1),
        end_date=date(2024, 3, 31),
        goal="Complete first 5K race",
        weekly_mileage_target=15.0,
        description="Progressive 8-week plan to build up to 5K distance"
    )
    storage.save_plan(plan)
    print("✓ Training plan created")
    
    # 6. Display Mike's training plan
    print("\n6. Mike's Training Plan:")
    mike_plans = storage.get_plans_for_runner("runner_002")
    for p in mike_plans:
        print(f"  Plan: {p.name}")
        print(f"  Goal: {p.goal}")
        print(f"  Duration: {p.start_date} to {p.end_date}")
        print(f"  Weekly Target: {p.weekly_mileage_target} km")
        print(f"  Description: {p.description}")
    
    # 7. Display statistics for Sarah
    print("\n7. Sarah's Statistics:")
    sarah_sessions = storage.get_sessions_for_runner("runner_001")
    total_distance = sum(s.distance_km for s in sarah_sessions)
    total_duration = sum(s.duration_minutes for s in sarah_sessions)
    avg_pace = total_duration / total_distance if total_distance > 0 else 0
    
    print(f"  Total Sessions: {len(sarah_sessions)}")
    print(f"  Total Distance: {total_distance:.1f} km")
    print(f"  Total Duration: {total_duration} minutes ({total_duration/60:.1f} hours)")
    print(f"  Average Pace: {avg_pace:.2f} min/km")
    
    print("\n" + "="*60)
    print("Demo completed successfully!")
    print("="*60)
    print("\nTo run the interactive application, use: python main.py")

if __name__ == "__main__":
    demo()
