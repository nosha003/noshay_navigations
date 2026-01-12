# Run Coaching Application

A simple and effective command-line application for managing run coaching programs. Track runners, log training sessions, create training plans, and monitor progress.

## Features

- **Runner Management**: Add and manage multiple runners/athletes
- **Training Session Logging**: Record runs with distance, duration, pace, and notes
- **Training Plans**: Create customized training plans with goals and weekly mileage targets
- **Statistics**: View comprehensive statistics for each runner
- **Data Persistence**: All data is stored locally in JSON format

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nosha003/noshay_navigations.git
cd noshay_navigations
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

### Main Menu Options

1. **Manage Runners**
   - Add new runners with name, email, age, and experience level
   - View all registered runners

2. **Log Training Session**
   - Record distance (km), duration (minutes), session type, and notes
   - Automatically calculates pace (min/km)
   - Session types: easy, tempo, interval, long, recovery

3. **View Training History**
   - See all training sessions for a runner
   - Displays date, distance, duration, pace, type, and notes

4. **Manage Training Plans**
   - Create training plans with start/end dates
   - Set goals and weekly mileage targets
   - View all plans for a runner

5. **View Runner Statistics**
   - Total sessions, distance, and duration
   - Average pace
   - Latest session information

## Data Storage

All data is stored in the `data/` directory as JSON files:
- `runners.json`: Runner/athlete information
- `sessions.json`: Training session records
- `plans.json`: Training plans

## Example Workflow

1. **Add a runner**: Choose option 1 → 1, enter runner details
2. **Log a training session**: Choose option 2, select runner, enter session details
3. **View progress**: Choose option 3 or 5 to see training history and statistics
4. **Create a training plan**: Choose option 4 → 1, define plan parameters

## Requirements

- Python 3.7+
- python-dateutil
- tabulate

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.