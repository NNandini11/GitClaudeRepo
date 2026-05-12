# UI Coding Standards

## Overview
This document outlines the coding standards for the UI throughout the Calendar Dashboard project. All frontend code must adhere to these standards to ensure consistency, maintainability, and accessibility.

## HTML Standards

### Structure
- Use semantic HTML5 elements (`<header>`, `<main>`, `<section>`, `<aside>`, etc.)
- Always include a `<!DOCTYPE html>` declaration
- Use proper meta tags for character encoding and viewport settings
- Maintain a logical document outline

### Accessibility
- Use proper heading hierarchy (h1, h2, h3, etc.)
- Add `alt` attributes to all images
- Use `<label>` elements associated with form inputs via `for` attribute
- Ensure sufficient color contrast (WCAG AA minimum 4.5:1 for text)
- Use semantic elements instead of divs for navigation, headers, and footers

### Naming Conventions
- Use kebab-case for CSS class names (e.g., `date-picker`, `main-content`)
- Use camelCase for JavaScript variable names
- Use descriptive names that reflect the element's purpose
- Avoid single-letter or abbreviated class names

## CSS Standards

### Organization
- Group related styles together
- Use a logical order: layout, box model, typography, visual effects
- Keep specificity low (avoid deep nesting and !important)
- Use CSS custom properties for repeated values and theming

### Naming Conventions
- Use BEM (Block, Element, Modifier) methodology for complex components
- Examples: `card`, `card__header`, `card--highlighted`
- Use descriptive names that are self-documenting

### Responsive Design
- Use mobile-first approach
- Use CSS Grid for layouts when appropriate
- Use Flexbox for alignment and spacing
- Use media queries for breakpoints (320px, 768px, 1024px, 1400px)

### Colors and Spacing
- Define a color palette as CSS variables
- Use consistent spacing units (8px, 16px, 24px, 32px)
- Ensure adequate whitespace for readability
- Use a consistent color scheme throughout the application

### Typography
- Use system fonts for better performance
- Limit to 2-3 font families per project
- Use appropriate font sizes for hierarchy (base: 16px, h1: 2.5rem, h2: 1.8rem, h3: 1.3rem)
- Ensure sufficient line height for readability (1.5 for body text)

## JavaScript Standards

### Code Style
- Use ES6+ features (arrow functions, const/let, template literals)
- Write self-documenting code with clear variable and function names
- Keep functions small and focused on a single responsibility
- Use async/await for asynchronous operations instead of callbacks

### DOM Manipulation
- Cache DOM selectors to avoid repeated queries
- Use `addEventListener` for event handling
- Avoid inline event handlers (onclick, onchange, etc.)
- Clean up event listeners when elements are removed

### Error Handling
- Validate user input before processing
- Provide user-friendly error messages
- Log errors to console for debugging
- Use try-catch blocks for error-prone operations

### Code Organization
- Group related functions together
- Use modules/namespacing to avoid global scope pollution
- Keep initialization logic separate from utility functions
- Document complex logic with comments only when necessary

## Component Standards

### Cards
- Use consistent padding (20px)
- Include shadows for depth (0 2px 4px rgba(0, 0, 0, 0.1))
- Add hover states for interactivity
- Ensure proper spacing between child elements (gap: 10-20px)

### Forms
- Use proper label associations
- Provide clear error messaging
- Show visual feedback for focused elements
- Use appropriate input types (date, email, number, etc.)

### Lists
- Use semantic `<ul>`, `<ol>`, or `<dl>` elements
- Style list items consistently
- Provide visual feedback on hover and focus

## Performance Standards

### Image Optimization
- Compress images before use
- Use appropriate image formats (WebP for modern browsers, PNG/JPG as fallback)
- Lazy load images below the fold

### CSS and JavaScript
- Minimize CSS and JavaScript files for production
- Avoid render-blocking resources
- Use CSS Grid and Flexbox instead of float-based layouts
- Debounce high-frequency events (scroll, resize, input)

## Testing Standards

### Visual Testing
- Test on multiple browsers (Chrome, Firefox, Safari, Edge)
- Test on multiple devices (mobile, tablet, desktop)
- Test all interactive elements
- Verify responsive design at all breakpoints

### Accessibility Testing
- Use accessibility checkers (axe, WAVE)
- Test keyboard navigation
- Test with screen readers
- Verify color contrast

## Naming Convention Summary

| Type | Convention | Example |
|------|-----------|---------|
| CSS Classes | kebab-case | `.date-picker`, `.main-content` |
| CSS IDs | camelCase | `#sessionsList` |
| JavaScript Variables | camelCase | `datePicker`, `selectedDate` |
| JavaScript Functions | camelCase | `loadDashboardData()`, `formatDate()` |
| Constants | UPPER_SNAKE_CASE | `MAX_RETRIES`, `API_ENDPOINT` |

## Example Component

```html
<!-- HTML -->
<div class="card">
    <h3 class="card__title">Sessions</h3>
    <div class="items-list" id="sessionsList">
        <p class="empty-message">No sessions</p>
    </div>
</div>
```

```css
/* CSS */
.card {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card__title {
    margin-bottom: 15px;
    font-size: 1.3rem;
    color: #667eea;
}

.items-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.empty-message {
    text-align: center;
    color: #999;
}
```

```javascript
// JavaScript
function loadDashboardData(date) {
    fetch(`/api/sessions?date=${date}`)
        .then(response => response.json())
        .then(data => displaySessions(data.sessions))
        .catch(error => console.error('Error:', error));
}
```
