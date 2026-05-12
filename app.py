from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from datetime import datetime
import MySQLdb.cursors
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'calendar_dashboard')

mysql = MySQL(app)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/sessions', methods=['GET'])
def get_sessions():
    date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))

    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        query = """
            SELECT * FROM sessions
            WHERE DATE(session_date) = %s
            ORDER BY session_time ASC
        """
        cursor.execute(query, (date_str,))
        sessions = cursor.fetchall()
        cursor.close()

        return jsonify({
            'success': True,
            'date': date_str,
            'sessions': sessions
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/events', methods=['GET'])
def get_events():
    date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))

    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        query = """
            SELECT * FROM events
            WHERE DATE(event_date) = %s
            ORDER BY event_time ASC
        """
        cursor.execute(query, (date_str,))
        events = cursor.fetchall()
        cursor.close()

        return jsonify({
            'success': True,
            'date': date_str,
            'events': events
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))

    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        query = """
            SELECT * FROM tasks
            WHERE DATE(task_date) = %s
            ORDER BY task_time ASC
        """
        cursor.execute(query, (date_str,))
        tasks = cursor.fetchall()
        cursor.close()

        return jsonify({
            'success': True,
            'date': date_str,
            'tasks': tasks
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/reminders', methods=['GET'])
def get_reminders():
    date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))

    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        query = """
            SELECT * FROM reminders
            WHERE DATE(reminder_date) = %s
            ORDER BY reminder_time ASC
        """
        cursor.execute(query, (date_str,))
        reminders = cursor.fetchall()
        cursor.close()

        return jsonify({
            'success': True,
            'date': date_str,
            'reminders': reminders
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
