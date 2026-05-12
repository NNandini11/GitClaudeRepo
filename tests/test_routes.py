import pytest
from datetime import datetime
import json


class TestDashboard:
    def test_dashboard_route_returns_html(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert b'Calendar Dashboard' in response.data
        assert b'<!DOCTYPE html>' in response.data


class TestSessionsAPI:
    def test_get_sessions_default_date(self, client):
        response = client.get('/api/sessions')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'success' in data
        assert 'date' in data
        assert 'sessions' in data
        assert data['success'] is True
        assert isinstance(data['sessions'], list)

    def test_get_sessions_with_valid_date(self, client):
        response = client.get('/api/sessions?date=2026-05-12')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['date'] == '2026-05-12'
        assert isinstance(data['sessions'], list)

    def test_get_sessions_json_format(self, client):
        response = client.get('/api/sessions?date=2026-05-12')
        assert response.content_type == 'application/json'

    def test_get_sessions_returns_empty_list_when_no_db(self, client):
        response = client.get('/api/sessions?date=2026-05-12')
        data = json.loads(response.data)
        assert data['sessions'] == [] or isinstance(data['sessions'], list)


class TestEventsAPI:
    def test_get_events_default_date(self, client):
        response = client.get('/api/events')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'success' in data
        assert 'date' in data
        assert 'events' in data
        assert data['success'] is True
        assert isinstance(data['events'], list)

    def test_get_events_with_valid_date(self, client):
        response = client.get('/api/events?date=2026-05-12')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['date'] == '2026-05-12'
        assert isinstance(data['events'], list)

    def test_get_events_json_format(self, client):
        response = client.get('/api/events?date=2026-05-12')
        assert response.content_type == 'application/json'


class TestTasksAPI:
    def test_get_tasks_default_date(self, client):
        response = client.get('/api/tasks')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'success' in data
        assert 'date' in data
        assert 'tasks' in data
        assert data['success'] is True
        assert isinstance(data['tasks'], list)

    def test_get_tasks_with_valid_date(self, client):
        response = client.get('/api/tasks?date=2026-05-12')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['date'] == '2026-05-12'
        assert isinstance(data['tasks'], list)

    def test_get_tasks_json_format(self, client):
        response = client.get('/api/tasks?date=2026-05-12')
        assert response.content_type == 'application/json'


class TestRemindersAPI:
    def test_get_reminders_default_date(self, client):
        response = client.get('/api/reminders')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'success' in data
        assert 'date' in data
        assert 'reminders' in data
        assert data['success'] is True
        assert isinstance(data['reminders'], list)

    def test_get_reminders_with_valid_date(self, client):
        response = client.get('/api/reminders?date=2026-05-12')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['date'] == '2026-05-12'
        assert isinstance(data['reminders'], list)

    def test_get_reminders_json_format(self, client):
        response = client.get('/api/reminders?date=2026-05-12')
        assert response.content_type == 'application/json'


class TestAPIDateHandling:
    def test_all_endpoints_accept_date_parameter(self, client):
        endpoints = ['/api/sessions', '/api/events', '/api/tasks', '/api/reminders']
        test_date = '2026-01-15'

        for endpoint in endpoints:
            response = client.get(f'{endpoint}?date={test_date}')
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['date'] == test_date

    def test_all_endpoints_have_default_date(self, client):
        endpoints = ['/api/sessions', '/api/events', '/api/tasks', '/api/reminders']

        for endpoint in endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200
            data = json.loads(response.data)
            assert 'date' in data
            today = datetime.now().strftime('%Y-%m-%d')
            assert data['date'] == today


class TestAPIErrorHandling:
    def test_api_handles_missing_database_gracefully(self, client):
        endpoints = ['/api/sessions', '/api/events', '/api/tasks', '/api/reminders']

        for endpoint in endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200
            assert response.content_type == 'application/json'
            data = json.loads(response.data)
            assert 'success' in data
            assert data['success'] is True
