import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import ItemsList from '../ItemsList'

describe('ItemsList', () => {
  it('renders the title', () => {
    render(<ItemsList title="Sessions" items={[]} />)
    expect(screen.getByText('Sessions')).toBeInTheDocument()
  })

  it('renders empty message when no items', () => {
    render(<ItemsList title="Events" items={[]} />)
    expect(screen.getByText('No events for this date')).toBeInTheDocument()
  })

  it('renders items correctly', () => {
    const items = [
      {
        title: 'Team Meeting',
        session_time: '10:00',
        description: 'Weekly sync'
      },
      {
        title: 'Code Review',
        session_time: '14:00',
        description: 'PR feedback'
      }
    ]

    render(<ItemsList title="Sessions" items={items} />)

    expect(screen.getByText('Team Meeting')).toBeInTheDocument()
    expect(screen.getByText('Code Review')).toBeInTheDocument()
    expect(screen.getByText('Weekly sync')).toBeInTheDocument()
    expect(screen.getByText('PR feedback')).toBeInTheDocument()
  })

  it('renders item times', () => {
    const items = [
      {
        title: 'Meeting',
        event_time: '15:30',
        description: 'Important'
      }
    ]

    render(<ItemsList title="Events" items={items} />)
    expect(screen.getByText('15:30')).toBeInTheDocument()
  })

  it('handles items without descriptions', () => {
    const items = [
      {
        title: 'Task',
        task_time: '11:00'
      }
    ]

    render(<ItemsList title="Tasks" items={items} />)
    expect(screen.getByText('Task')).toBeInTheDocument()
    expect(screen.getByText('11:00')).toBeInTheDocument()
  })

  it('handles items without times', () => {
    const items = [
      {
        title: 'Reminder'
      }
    ]

    render(<ItemsList title="Reminders" items={items} />)
    expect(screen.getByText('Reminder')).toBeInTheDocument()
    expect(screen.getByText('N/A')).toBeInTheDocument()
  })
})
