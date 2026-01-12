"""Command-line interface for the run coaching application."""

import sys
from datetime import datetime, date
from typing import Optional
from run_coaching.models import Runner, TrainingSession, TrainingPlan
from run_coaching.storage import Storage
from tabulate import tabulate


class CoachingCLI:
    """Command-line interface for the run coaching application."""
    
    def __init__(self):
        """Initialize the CLI with storage."""
        self.storage = Storage()
    
    def print_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("Run Coaching Application")
        print("="*50)
        print("1. Manage Runners")
        print("2. Log Training Session")
        print("3. View Training History")
        print("4. Manage Training Plans")
        print("5. View Runner Statistics")
        print("0. Exit")
        print("="*50)
    
    def manage_runners_menu(self):
        """Display and handle runner management menu."""
        while True:
            print("\n--- Manage Runners ---")
            print("1. Add New Runner")
            print("2. View All Runners")
            print("0. Back to Main Menu")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                self.add_runner()
            elif choice == "2":
                self.view_all_runners()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def add_runner(self):
        """Add a new runner."""
        print("\n--- Add New Runner ---")
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        
        # Validate age input
        while True:
            try:
                age = int(input("Age: ").strip())
                if age <= 0 or age > 120:
                    print("Please enter a valid age between 1 and 120.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Validate experience level
        valid_levels = ["beginner", "intermediate", "advanced"]
        print(f"Experience Level: {', '.join(valid_levels)}")
        while True:
            experience_level = input("Experience Level: ").strip().lower()
            if experience_level in valid_levels:
                break
            print(f"Invalid level. Please choose from: {', '.join(valid_levels)}")
        
        runner_id = f"runner_{len(self.storage.get_all_runners()) + 1}"
        runner = Runner(
            id=runner_id,
            name=name,
            email=email,
            age=age,
            experience_level=experience_level
        )
        
        self.storage.save_runner(runner)
        print(f"\n✓ Runner added successfully! ID: {runner_id}")
    
    def view_all_runners(self):
        """View all runners."""
        runners = self.storage.get_all_runners()
        if not runners:
            print("\nNo runners found.")
            return
        
        print("\n--- All Runners ---")
        table_data = []
        for runner in runners:
            table_data.append([
                runner.id,
                runner.name,
                runner.email,
                runner.age,
                runner.experience_level
            ])
        
        print(tabulate(table_data, 
                      headers=["ID", "Name", "Email", "Age", "Level"],
                      tablefmt="grid"))
    
    def log_training_session(self):
        """Log a new training session."""
        runners = self.storage.get_all_runners()
        if not runners:
            print("\nNo runners found. Please add a runner first.")
            return
        
        print("\n--- Log Training Session ---")
        self.view_all_runners()
        
        runner_id = input("\nEnter Runner ID: ").strip()
        runner = self.storage.get_runner_by_id(runner_id)
        if not runner:
            print("Runner not found.")
            return
        
        # Validate date input
        while True:
            date_str = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
            if not date_str:
                session_date = date.today()
                break
            try:
                session_date = date.fromisoformat(date_str)
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")
        
        # Validate distance input
        while True:
            try:
                distance_km = float(input("Distance (km): ").strip())
                if distance_km <= 0:
                    print("Distance must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Validate duration input
        while True:
            try:
                duration_minutes = int(input("Duration (minutes): ").strip())
                if duration_minutes <= 0:
                    print("Duration must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Validate session type
        valid_types = ["easy", "tempo", "interval", "long", "recovery"]
        print(f"Session Type: {', '.join(valid_types)}")
        while True:
            session_type = input("Session Type: ").strip().lower()
            if session_type in valid_types:
                break
            print(f"Invalid type. Please choose from: {', '.join(valid_types)}")
        
        notes = input("Notes (optional): ").strip()
        
        sessions = self.storage.get_sessions_for_runner(runner_id)
        session_id = f"session_{runner_id}_{len(sessions) + 1}"
        
        session = TrainingSession(
            id=session_id,
            runner_id=runner_id,
            date=session_date,
            distance_km=distance_km,
            duration_minutes=duration_minutes,
            session_type=session_type,
            notes=notes
        )
        
        self.storage.save_session(session)
        print(f"\n✓ Training session logged successfully!")
        print(f"  Pace: {session.pace_min_per_km:.2f} min/km")
    
    def view_training_history(self):
        """View training history for a runner."""
        runners = self.storage.get_all_runners()
        if not runners:
            print("\nNo runners found.")
            return
        
        print("\n--- View Training History ---")
        self.view_all_runners()
        
        runner_id = input("\nEnter Runner ID: ").strip()
        runner = self.storage.get_runner_by_id(runner_id)
        if not runner:
            print("Runner not found.")
            return
        
        sessions = self.storage.get_sessions_for_runner(runner_id)
        if not sessions:
            print(f"\nNo training sessions found for {runner.name}.")
            return
        
        print(f"\n--- Training History for {runner.name} ---")
        table_data = []
        for session in sessions:
            table_data.append([
                session.date,
                f"{session.distance_km:.2f}",
                session.duration_minutes,
                f"{session.pace_min_per_km:.2f}" if session.pace_min_per_km else "N/A",
                session.session_type,
                session.notes[:30] + "..." if len(session.notes) > 30 else session.notes
            ])
        
        print(tabulate(table_data,
                      headers=["Date", "Distance (km)", "Duration (min)", 
                              "Pace (min/km)", "Type", "Notes"],
                      tablefmt="grid"))
    
    def manage_training_plans_menu(self):
        """Display and handle training plan management menu."""
        while True:
            print("\n--- Manage Training Plans ---")
            print("1. Create Training Plan")
            print("2. View Training Plans")
            print("0. Back to Main Menu")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                self.create_training_plan()
            elif choice == "2":
                self.view_training_plans()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def create_training_plan(self):
        """Create a new training plan."""
        runners = self.storage.get_all_runners()
        if not runners:
            print("\nNo runners found. Please add a runner first.")
            return
        
        print("\n--- Create Training Plan ---")
        self.view_all_runners()
        
        runner_id = input("\nEnter Runner ID: ").strip()
        runner = self.storage.get_runner_by_id(runner_id)
        if not runner:
            print("Runner not found.")
            return
        
        name = input("Plan Name: ").strip()
        
        # Validate start date
        while True:
            start_date_str = input("Start Date (YYYY-MM-DD): ").strip()
            try:
                start_date = date.fromisoformat(start_date_str)
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")
        
        # Validate end date
        while True:
            end_date_str = input("End Date (YYYY-MM-DD): ").strip()
            try:
                end_date = date.fromisoformat(end_date_str)
                if end_date <= start_date:
                    print("End date must be after start date.")
                    continue
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")
        
        goal = input("Goal: ").strip()
        
        # Validate weekly mileage
        while True:
            try:
                weekly_mileage = float(input("Weekly Mileage Target (km): ").strip())
                if weekly_mileage <= 0:
                    print("Weekly mileage must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        description = input("Description (optional): ").strip()
        
        plans = self.storage.get_plans_for_runner(runner_id)
        plan_id = f"plan_{runner_id}_{len(plans) + 1}"
        
        plan = TrainingPlan(
            id=plan_id,
            runner_id=runner_id,
            name=name,
            start_date=start_date,
            end_date=end_date,
            goal=goal,
            weekly_mileage_target=weekly_mileage,
            description=description
        )
        
        self.storage.save_plan(plan)
        print(f"\n✓ Training plan created successfully! ID: {plan_id}")
    
    def view_training_plans(self):
        """View training plans for a runner."""
        runners = self.storage.get_all_runners()
        if not runners:
            print("\nNo runners found.")
            return
        
        print("\n--- View Training Plans ---")
        self.view_all_runners()
        
        runner_id = input("\nEnter Runner ID: ").strip()
        runner = self.storage.get_runner_by_id(runner_id)
        if not runner:
            print("Runner not found.")
            return
        
        plans = self.storage.get_plans_for_runner(runner_id)
        if not plans:
            print(f"\nNo training plans found for {runner.name}.")
            return
        
        print(f"\n--- Training Plans for {runner.name} ---")
        for plan in plans:
            print(f"\nPlan: {plan.name}")
            print(f"  Goal: {plan.goal}")
            print(f"  Duration: {plan.start_date} to {plan.end_date}")
            print(f"  Weekly Target: {plan.weekly_mileage_target} km")
            if plan.description:
                print(f"  Description: {plan.description}")
    
    def view_runner_statistics(self):
        """View statistics for a runner."""
        runners = self.storage.get_all_runners()
        if not runners:
            print("\nNo runners found.")
            return
        
        print("\n--- View Runner Statistics ---")
        self.view_all_runners()
        
        runner_id = input("\nEnter Runner ID: ").strip()
        runner = self.storage.get_runner_by_id(runner_id)
        if not runner:
            print("Runner not found.")
            return
        
        sessions = self.storage.get_sessions_for_runner(runner_id)
        if not sessions:
            print(f"\nNo training sessions found for {runner.name}.")
            return
        
        total_distance = sum(s.distance_km for s in sessions)
        total_duration = sum(s.duration_minutes for s in sessions)
        avg_pace = total_duration / total_distance if total_distance > 0 else 0
        
        print(f"\n--- Statistics for {runner.name} ---")
        print(f"Total Sessions: {len(sessions)}")
        print(f"Total Distance: {total_distance:.2f} km")
        print(f"Total Duration: {total_duration} minutes ({total_duration/60:.2f} hours)")
        print(f"Average Pace: {avg_pace:.2f} min/km")
        
        if sessions:
            print(f"Latest Session: {sessions[0].date} - {sessions[0].distance_km:.2f} km")
    
    def run(self):
        """Run the CLI application."""
        print("\nWelcome to the Run Coaching Application!")
        
        while True:
            self.print_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                self.manage_runners_menu()
            elif choice == "2":
                self.log_training_session()
            elif choice == "3":
                self.view_training_history()
            elif choice == "4":
                self.manage_training_plans_menu()
            elif choice == "5":
                self.view_runner_statistics()
            elif choice == "0":
                print("\nThank you for using the Run Coaching Application!")
                sys.exit(0)
            else:
                print("\nInvalid choice. Please try again.")


def main():
    """Main entry point for the CLI application."""
    cli = CoachingCLI()
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\n\nExiting... Thank you for using the Run Coaching Application!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
