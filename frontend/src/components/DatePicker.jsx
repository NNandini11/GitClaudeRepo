export default function DatePicker({ selectedDate, onDateChange }) {
  return (
    <div className="date-picker-section">
      <label htmlFor="datePicker">Select Date:</label>
      <input
        type="date"
        id="datePicker"
        className="date-picker"
        value={selectedDate}
        onChange={(e) => onDateChange(e.target.value)}
      />
    </div>
  )
}
