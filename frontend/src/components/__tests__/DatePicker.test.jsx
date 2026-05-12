import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import DatePicker from '../DatePicker'

describe('DatePicker', () => {
  it('renders date picker input', () => {
    const mockOnDateChange = vi.fn()
    render(<DatePicker selectedDate="2026-05-12" onDateChange={mockOnDateChange} />)

    const input = screen.getByRole('textbox')
    expect(input).toBeInTheDocument()
  })

  it('displays the selected date', () => {
    const mockOnDateChange = vi.fn()
    render(<DatePicker selectedDate="2026-05-12" onDateChange={mockOnDateChange} />)

    const input = screen.getByDisplayValue('2026-05-12')
    expect(input).toBeInTheDocument()
  })

  it('calls onDateChange when date is changed', async () => {
    const user = userEvent.setup()
    const mockOnDateChange = vi.fn()
    render(<DatePicker selectedDate="2026-05-12" onDateChange={mockOnDateChange} />)

    const input = screen.getByRole('textbox')
    await user.clear(input)
    await user.type(input, '2026-06-15')

    expect(mockOnDateChange).toHaveBeenCalledWith('2026-06-15')
  })

  it('has a label associated with the input', () => {
    const mockOnDateChange = vi.fn()
    render(<DatePicker selectedDate="2026-05-12" onDateChange={mockOnDateChange} />)

    const label = screen.getByLabelText('Select Date:')
    expect(label).toBeInTheDocument()
  })
})
