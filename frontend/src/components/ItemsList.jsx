export default function ItemsList({ title, items }) {
  return (
    <div className="card">
      <h3>{title}</h3>
      <div className="items-list">
        {items.length === 0 ? (
          <p className="empty-message">No {title.toLowerCase()} for this date</p>
        ) : (
          items.map((item, idx) => (
            <div key={idx} className="item">
              <div className="item-title">{item.title || 'Untitled'}</div>
              <div className="item-time">
                {item.session_time || item.event_time || item.task_time || item.reminder_time || 'N/A'}
              </div>
              {(item.description || item.location) && (
                <div className="item-description">
                  {item.description || item.location}
                </div>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  )
}
