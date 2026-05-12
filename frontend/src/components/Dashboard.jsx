import { useState, useEffect } from 'react'
import './Dashboard.css'
import DatePicker from './DatePicker'
import SessionsList from './SessionsList'
import EventsList from './EventsList'
import TasksList from './TasksList'
import RemindersList from './RemindersList'

export default function Dashboard() {
  const [selectedDate, setSelectedDate] = useState(new Date().toISOString().split('T')[0])
  const [sessions, setSessions] = useState([])
  const [events, setEvents] = useState([])
  const [tasks, setTasks] = useState([])
  const [reminders, setReminders] = useState([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    loadDashboardData(selectedDate)
  }, [selectedDate])

  const loadDashboardData = async (date) => {
    setLoading(true)
    try {
      const [sessionsRes, eventsRes, tasksRes, remindersRes] = await Promise.all([
        fetch(`/api/sessions?date=${date}`),
        fetch(`/api/events?date=${date}`),
        fetch(`/api/tasks?date=${date}`),
        fetch(`/api/reminders?date=${date}`)
      ])

      const sessionsData = await sessionsRes.json()
      const eventsData = await eventsRes.json()
      const tasksData = await tasksRes.json()
      const remindersData = await remindersRes.json()

      setSessions(sessionsData.sessions || [])
      setEvents(eventsData.events || [])
      setTasks(tasksData.tasks || [])
      setReminders(remindersData.reminders || [])
    } catch (error) {
      console.error('Error loading dashboard data:', error)
    } finally {
      setLoading(false)
    }
  }

  const formatDate = (dateString) => {
    const date = new Date(dateString + 'T00:00:00')
    return date.toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    })
  }

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>Calendar Dashboard</h1>
      </header>

      <div className="dashboard-container">
        <aside className="dashboard-sidebar">
          <DatePicker selectedDate={selectedDate} onDateChange={setSelectedDate} />
        </aside>

        <main className="dashboard-main">
          <div className="date-display">
            <h2>{formatDate(selectedDate)}</h2>
          </div>

          {loading && <div className="loading">Loading...</div>}

          <div className="dashboard-grid">
            <SessionsList sessions={sessions} />
            <EventsList events={events} />
            <TasksList tasks={tasks} />
            <RemindersList reminders={reminders} />
          </div>
        </main>
      </div>
    </div>
  )
}
