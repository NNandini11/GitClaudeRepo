# Testing Guide

## Overview

This project includes comprehensive unit tests for both the Flask backend and React frontend.

## Backend Tests (Flask)

### Running Backend Tests

```bash
# Activate virtual environment
source venv/bin/activate

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_routes.py

# Run specific test class
pytest tests/test_routes.py::TestDashboard

# Run specific test
pytest tests/test_routes.py::TestDashboard::test_dashboard_route_returns_html
```

### Test Structure

```
tests/
├── __init__.py
├── conftest.py          # Pytest fixtures and configuration
└── test_routes.py       # API endpoint tests
```

### Backend Test Coverage

The backend tests cover:

- **Dashboard Route** - HTML rendering and structure
- **Sessions API** - GET /api/sessions endpoint
- **Events API** - GET /api/events endpoint
- **Tasks API** - GET /api/tasks endpoint
- **Reminders API** - GET /api/reminders endpoint
- **Date Handling** - Default and custom date parameters
- **Error Handling** - Graceful degradation when database is unavailable

**Current Coverage:** 82%

### Key Test Classes

1. **TestDashboard** - Dashboard page rendering
2. **TestSessionsAPI** - Sessions endpoint tests
3. **TestEventsAPI** - Events endpoint tests
4. **TestTasksAPI** - Tasks endpoint tests
5. **TestRemindersAPI** - Reminders endpoint tests
6. **TestAPIDateHandling** - Date parameter validation
7. **TestAPIErrorHandling** - Error scenarios

## Frontend Tests (React)

### Setup Frontend Tests

```bash
cd frontend

# Install testing dependencies
npm install --save-dev vitest @testing-library/react @testing-library/jest-dom @testing-library/user-event jsdom @vitest/ui

# Run tests
npm test

# Run with UI
npm run test:ui

# Run with coverage
npm run test:coverage
```

### Frontend Test Structure

```
frontend/src/components/__tests__/
├── DatePicker.test.jsx   # DatePicker component tests
└── ItemsList.test.jsx    # ItemsList component tests
```

### Frontend Test Coverage

The frontend tests cover:

- **DatePicker Component**
  - Input rendering
  - Selected date display
  - Date change callbacks
  - Label association

- **ItemsList Component**
  - Title rendering
  - Empty state messages
  - Item rendering
  - Item times and descriptions
  - Missing data handling

### Running Specific Frontend Tests

```bash
cd frontend

# Run all tests
npm test

# Run single test file
npm test DatePicker.test.jsx

# Run with UI
npm run test:ui

# Run with coverage report
npm run test:coverage
```

## Test Statistics

### Backend Tests
- **Total Tests:** 17
- **Passed:** 17
- **Failed:** 0
- **Coverage:** 82%
- **Execution Time:** < 1 second

### Frontend Tests
- **Total Tests:** 11 (ready to run after setup)
- **Categories:** DatePicker (5), ItemsList (6)

## CI/CD Integration

To integrate tests into CI/CD pipeline:

```yaml
# Example GitHub Actions workflow
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - run: pip install -r requirements.txt
      - run: pytest
      - uses: actions/setup-node@v2
        with:
          node-version: 18
      - run: cd frontend && npm install && npm test
```

## Test Best Practices

### For Backend Tests
- Test one thing per test function
- Use descriptive test names
- Mock external dependencies
- Test both happy and error paths
- Verify response structure and content

### For Frontend Tests
- Test user interactions
- Test component rendering
- Use semantic queries (getByRole, getByLabelText)
- Test accessibility features
- Mock API calls when needed

## Troubleshooting

### Backend Tests
- Ensure pytest is installed: `pip install pytest pytest-cov`
- Check that conftest.py is in the tests directory
- Verify Flask app can be imported from the test directory

### Frontend Tests
- Ensure all test dependencies are installed
- Vitest requires Node 14.16+
- JSdom environment must be specified in config

## Coverage Goals

- **Backend:** Target 85%+ coverage
- **Frontend:** Target 80%+ coverage
- Critical paths: 100% coverage

## Adding New Tests

### Backend
1. Add test function to appropriate test class in `tests/test_routes.py`
2. Use the `client` fixture from `conftest.py`
3. Follow naming convention: `test_<what_is_being_tested>`
4. Run `pytest` to verify

### Frontend
1. Create test file in `src/components/__tests__/`
2. Import necessary testing utilities
3. Use `describe` and `it` blocks
4. Use semantic queries for DOM elements
5. Run `npm test` to verify

## Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Vitest Documentation](https://vitest.dev/)
- [React Testing Library](https://testing-library.com/react)
- [Flask Testing](https://flask.palletsprojects.com/testing/)
