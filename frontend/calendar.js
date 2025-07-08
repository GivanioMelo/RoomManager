function pageLoad() {
    today = new Date();
    document.getElementById('currentMonth').value = today.getMonth() + 1; // Months are 0-indexed
    document.getElementById('currentYear').value = today.getFullYear();
    updateCalendarGrid();
}

function updateCalendarGrid() {
    const calendarGrid = document.getElementById('calendarGrid');
    calendarGrid.innerHTML = ''; // Clear previous content
    let rowOffset = 0;
    const currentMonth = document.getElementById('currentMonth').value;
    const currentYear = document.getElementById('currentYear').value;
    document.getElementById('currentMonthDisplay').textContent = new Date(currentYear, currentMonth - 1).toLocaleString('default', { month: 'long' }) + ' ' + currentYear;
    rowsStart = 2; // Start from the second row for the days
    for (let i = 0; i < 31; i++) {    
        const date = new Date(currentYear, currentMonth - 1, i + 1);
        const weekday = date.getDay()+1;

        if (date.getMonth() !== currentMonth - 1) continue; // Skip days that are not in the current month

        console.log("Date: " + date.toDateString() + ", Weekday: " + weekday);

        const dayCell = document.createElement('div');
        dayCell.className = 'day-cell';
        dayCell.style.gridColumnStart = weekday; // Adjust for CSS grid
        dayCell.style.gridRowStart = rowsStart;
        if (weekday == 7) rowsStart++; // Move to the next row after Saturday
        dayCell.textContent = date; // Placeholder for day numbers
        calendarGrid.appendChild(dayCell);
    }
}

function nextMonth() {
    let currentMonth = parseInt(document.getElementById('currentMonth').value);
    let currentYear = parseInt(document.getElementById('currentYear').value);
        
    if (currentMonth === 12)
    {
        currentMonth = 1;
        currentYear += 1;
    }
    else
    {
        currentMonth += 1;
    }

    document.getElementById('currentMonth').value = currentMonth;
    document.getElementById('currentYear').value = currentYear;
    updateCalendarGrid();
}

function previousMonth() {
    let currentMonth = parseInt(document.getElementById('currentMonth').value);
    let currentYear = parseInt(document.getElementById('currentYear').value);
        
    if (currentMonth === 1)
    {
        currentMonth = 12;
        currentYear -= 1;
    }
    else
    {
        currentMonth -= 1;
    }

    document.getElementById('currentMonth').value = currentMonth;
    document.getElementById('currentYear').value = currentYear;
    updateCalendarGrid();
}