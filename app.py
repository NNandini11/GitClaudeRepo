from flask import Flask, render_template, request, jsonify
from datetime import datetime
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
MYSQL_DB = os.getenv('MYSQL_DB', 'calendar_dashboard')

def get_db_connection():
    try:
        return pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB,
            cursorclass=pymysql.cursors.DictCursor
        )
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/sessions', methods=['GET'])
def get_sessions():
    date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))

    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({
                'success': True,
                'date': date_str,
                'sessions': []
            })

        cursor = conn.cursor()
        query = """
            SELECT * FROM sessions
            WHERE DATE(session_date) = %s
            ORDER BY session_time ASC
        """
        cursor.execute(query, (date_str,))
        sessions = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify({
            'success': True,
            'date': date_str,
            'sessions': sessions
        })
    except Exception as e:
        return jsonify({
            'success': True,
            'date': date_str,
            'sessions': []
        })

@app.route('/api/events', methods=['GET'])
def get_events():
    date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))

    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({
                'success': True,
                'date': date_str,
                'events': []
            })

        cursor = conn.cursor()
        query = """
            SELECT * FROM events
            WHERE DATE(event_date) = %s
            ORDER BY event_time ASC
        """
        cursor.execute(query, (date_str,))
        events = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify({
            'success': True,
            'date': date_str,
            'events': events
        })
    except Exception as e:
        return jsonify({
            'success': True,
            'date': date_str,
            'events': []
        })

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))

    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({
                'success': True,
                'date': date_str,
                'tasks': []
            })

        cursor = conn.cursor()
        query = """
            SELECT * FROM tasks
            WHERE DATE(task_date) = %s
            ORDER BY task_time ASC
        """
        cursor.execute(query, (date_str,))
        tasks = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify({
            'success': True,
            'date': date_str,
            'tasks': tasks
        })
    except Exception as e:
        return jsonify({
            'success': True,
            'date': date_str,
            'tasks': []
        })

@app.route('/api/reminders', methods=['GET'])
def get_reminders():
    date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))

    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({
                'success': True,
                'date': date_str,
                'reminders': []
            })

        cursor = conn.cursor()
        query = """
            SELECT * FROM reminders
            WHERE DATE(reminder_date) = %s
            ORDER BY reminder_time ASC
        """
        cursor.execute(query, (date_str,))
        reminders = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify({
            'success': True,
            'date': date_str,
            'reminders': reminders
        })
    except Exception as e:
        return jsonify({
            'success': True,
            'date': date_str,
            'reminders': []
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
