# Calendar Dashboard Setup Guide

## Prerequisites
- Python 3.7+
- MySQL 5.7+
- pip (Python package manager)

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/NNandini11/GitClaudeRepo.git
cd GitClaudeRepo
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your MySQL credentials:
   ```
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=your_password
   MYSQL_DB=calendar_dashboard
   ```

3. Create the database and tables:
   ```bash
   mysql -u root -p < database_schema.sql
   ```

### 5. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Features

### Dashboard Page
- **Date Picker**: Select any date to view schedule
- **Default View**: Shows current date on page load
- **Sessions**: Display all sessions for the selected date
- **Events**: Display all events for the selected date
- **Tasks**: Display all tasks for the selected date
- **Reminders**: Display all reminders for the selected date

### API Endpoints

#### Get Sessions
```
GET /api/sessions?date=YYYY-MM-DD
Response: { success: boolean, date: string, sessions: array }
```

#### Get Events
```
GET /api/events?date=YYYY-MM-DD
Response: { success: boolean, date: string, events: array }
```

#### Get Tasks
```
GET /api/tasks?date=YYYY-MM-DD
Response: { success: boolean, date: string, tasks: array }
```

#### Get Reminders
```
GET /api/reminders?date=YYYY-MM-DD
Response: { success: boolean, date: string, reminders: array }
```

## Project Structure

```
calendar-dashboard/
├── app.py                    # Flask application and routes
├── requirements.txt          # Python dependencies
├── database_schema.sql       # MySQL database schema
├── .env.example              # Environment variables template
├── SETUP.md                  # Setup instructions
├── docs/
│   └── ui.md                 # UI coding standards
├── templates/
│   └── dashboard.html        # Main dashboard template
└── static/
    ├── styles.css            # Stylesheet
    └── script.js             # Client-side JavaScript
```

## Database Schema

### Tables

#### sessions
- `id`: Primary key
- `title`: Session title
- `description`: Session description
- `session_date`: Date of the session
- `session_time`: Time of the session

#### events
- `id`: Primary key
- `title`: Event title
- `description`: Event description
- `event_date`: Date of the event
- `event_time`: Time of the event
- `location`: Event location

#### tasks
- `id`: Primary key
- `title`: Task title
- `description`: Task description
- `task_date`: Date of the task
- `task_time`: Time of the task
- `priority`: low, medium, or high
- `status`: pending, in_progress, or completed

#### reminders
- `id`: Primary key
- `title`: Reminder title
- `description`: Reminder description
- `reminder_date`: Date of the reminder
- `reminder_time`: Time of the reminder
- `type`: email, notification, or sms

## Testing

### Sample Data
You can insert sample data for testing:

```sql
INSERT INTO sessions (title, description, session_date, session_time)
VALUES ('Team Meeting', 'Weekly sync', NOW(), '10:00:00');

INSERT INTO events (title, event_date, event_time, location)
VALUES ('Project Kickoff', NOW(), '14:00:00', 'Conference Room A');

INSERT INTO tasks (title, task_date, task_time, priority, status)
VALUES ('Review PR', NOW(), '15:00:00', 'high', 'pending');

INSERT INTO reminders (title, reminder_date, reminder_time, type)
VALUES ('Submit report', NOW(), '17:00:00', 'notification');
```

## Troubleshooting

### MySQL Connection Error
- Verify MySQL is running
- Check credentials in `.env` file
- Ensure database exists: `SHOW DATABASES;`

### Port Already in Use
- Flask defaults to port 5000
- Change port in `app.py`: `app.run(port=5001)`

### Module Import Errors
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

## UI Styling

The dashboard uses a modern, responsive design with:
- Gradient header with purple theme
- Card-based layout for content sections
- Responsive grid system (mobile-first)
- Smooth transitions and hover effects
- Accessible color contrast and typography

See `docs/ui.md` for detailed UI coding standards.

## Support

For issues or questions, please refer to:
- `docs/ui.md` - UI coding standards
- `SETUP.md` - This file
- `app.py` - Application code and API endpoints
