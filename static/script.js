document.addEventListener('DOMContentLoaded', function() {
    const datePicker = document.getElementById('datePicker');
    const selectedDateDisplay = document.getElementById('selectedDate');
    const sessionsList = document.getElementById('sessionsList');
    const eventsList = document.getElementById('eventsList');
    const tasksList = document.getElementById('tasksList');
    const remindersList = document.getElementById('remindersList');

    function formatDate(dateString) {
        const date = new Date(dateString + 'T00:00:00');
        return date.toLocaleDateString('en-US', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    }

    function setDefaultDate() {
        const today = new Date();
        const year = today.getFullYear();
        const month = String(today.getMonth() + 1).padStart(2, '0');
        const day = String(today.getDate()).padStart(2, '0');
        const dateString = `${year}-${month}-${day}`;

        datePicker.value = dateString;
        selectedDateDisplay.textContent = formatDate(dateString);
        loadDashboardData(dateString);
    }

    function loadDashboardData(date) {
        Promise.all([
            fetch(`/api/sessions?date=${date}`).then(r => r.json()),
            fetch(`/api/events?date=${date}`).then(r => r.json()),
            fetch(`/api/tasks?date=${date}`).then(r => r.json()),
            fetch(`/api/reminders?date=${date}`).then(r => r.json())
        ]).then(([sessionsData, eventsData, tasksData, remindersData]) => {
            displaySessions(sessionsData.sessions || []);
            displayEvents(eventsData.events || []);
            displayTasks(tasksData.tasks || []);
            displayReminders(remindersData.reminders || []);
        }).catch(error => {
            console.error('Error loading dashboard data:', error);
            sessionsList.innerHTML = '<p class="empty-message">Error loading sessions</p>';
            eventsList.innerHTML = '<p class="empty-message">Error loading events</p>';
            tasksList.innerHTML = '<p class="empty-message">Error loading tasks</p>';
            remindersList.innerHTML = '<p class="empty-message">Error loading reminders</p>';
        });
    }

    function displaySessions(sessions) {
        if (sessions.length === 0) {
            sessionsList.innerHTML = '<p class="empty-message">No sessions for this date</p>';
            return;
        }

        sessionsList.innerHTML = sessions.map(session => `
            <div class="item">
                <div class="item-title">${escapeHtml(session.title || 'Untitled')}</div>
                <div class="item-time">${session.session_time || 'N/A'}</div>
                ${session.description ? `<div class="item-description">${escapeHtml(session.description)}</div>` : ''}
            </div>
        `).join('');
    }

    function displayEvents(events) {
        if (events.length === 0) {
            eventsList.innerHTML = '<p class="empty-message">No events for this date</p>';
            return;
        }

        eventsList.innerHTML = events.map(event => `
            <div class="item">
                <div class="item-title">${escapeHtml(event.title || 'Untitled')}</div>
                <div class="item-time">${event.event_time || 'N/A'}</div>
                ${event.description ? `<div class="item-description">${escapeHtml(event.description)}</div>` : ''}
            </div>
        `).join('');
    }

    function displayTasks(tasks) {
        if (tasks.length === 0) {
            tasksList.innerHTML = '<p class="empty-message">No tasks for this date</p>';
            return;
        }

        tasksList.innerHTML = tasks.map(task => `
            <div class="item">
                <div class="item-title">${escapeHtml(task.title || 'Untitled')}</div>
                <div class="item-time">${task.task_time || 'N/A'}</div>
                ${task.description ? `<div class="item-description">${escapeHtml(task.description)}</div>` : ''}
            </div>
        `).join('');
    }

    function displayReminders(reminders) {
        if (reminders.length === 0) {
            remindersList.innerHTML = '<p class="empty-message">No reminders for this date</p>';
            return;
        }

        remindersList.innerHTML = reminders.map(reminder => `
            <div class="item">
                <div class="item-title">${escapeHtml(reminder.title || 'Untitled')}</div>
                <div class="item-time">${reminder.reminder_time || 'N/A'}</div>
                ${reminder.description ? `<div class="item-description">${escapeHtml(reminder.description)}</div>` : ''}
            </div>
        `).join('');
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    datePicker.addEventListener('change', function() {
        const selectedDate = this.value;
        selectedDateDisplay.textContent = formatDate(selectedDate);
        loadDashboardData(selectedDate);
    });

    setDefaultDate();
});
