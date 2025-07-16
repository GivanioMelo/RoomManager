reserves = [
    {user:'Alice', month:7, day: 9, startTime: "08:00", endTime: "12:00" },
    {user:'Dave', month:7, day: 9, startTime: "18:00", endTime: "22:00" },
];

function pageLoad() {
    let today = new Date();
    let roomId = localStorage.getItem("roomId");
    if (!roomId) {window.location.href = "map.html"; return;}
    
    updateCalendarGrid();
}

function openDayProgram(day, month) {
    let roomId = localStorage.getItem("roomId");
    if (!roomId) {window.location.href = "map.html"; return;}
    let selectedDate = new Date(new Date().getFullYear(), month - 1, day);
    localStorage.setItem("selectedDate", selectedDate.toISOString().split('T')[0]); // Store date in YYYY-MM-DD format
    window.location.href = "day.html";
}

function updateCalendarGrid() {
    const calendarGrid = document.getElementById('calendarGrid');
    calendarGrid.innerHTML = ''; // Clear previous content
    let rowOffset = 0;
    
    let currentMonth = parseInt(localStorage.getItem('currentMonth')) || new Date().getMonth() + 1; // Months are 0-indexed
    let currentYear = parseInt(localStorage.getItem('currentYear')) || new Date().getFullYear();

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
        dayCell.textContent = i; // Placeholder for day numbers

        for (const reserve of reserves) {
            if (reserve.month === currentMonth && reserve.day === i) {
                const reserveBox = document.createElement('div');
                reserveBox.className = 'reserve';
                reserveBox.textContent = `${reserve.user} ${reserve.startTime} - ${reserve.endTime}`;
                reserveBox.style.gridRowStart = rowsStart;
                reserveBox.style.gridColumnStart = weekday;
                reserveBox.style.gridColumnEnd = weekday + 1; // Span one column
                reserveBox.style.position = 'relative';
                reserveBox.style.zIndex = '2'; // Ensure it floats above day cell
                dayCell.appendChild(reserveBox);
            }
        }

        calendarGrid.appendChild(dayCell);
    }
}

function nextMonth() {
    let currentMonth = parseInt(localStorage.getItem('currentMonth')) || new Date().getMonth() + 1; // Months are 0-indexed
    let currentYear = parseInt(localStorage.getItem('currentYear')) || new Date().getFullYear();
    
    if (currentMonth === 12)
    {
        currentMonth = 1;
        currentYear += 1;
    }
    else
    {
        currentMonth += 1;
    }

    localStorage.setItem('currentMonth', currentMonth);
    localStorage.setItem('currentYear', currentYear);
    updateCalendarGrid();
}

function previousMonth() {
    let currentMonth = parseInt(localStorage.getItem('currentMonth')) || new Date().getMonth() + 1; // Months are 0-indexed
    let currentYear = parseInt(localStorage.getItem('currentYear')) || new Date().getFullYear();
        
    if (currentMonth === 1)
    {
        currentMonth = 12;
        currentYear -= 1;
    }
    else
    {
        currentMonth -= 1;
    }

    localStorage.setItem('currentMonth', currentMonth);
    localStorage.setItem('currentYear', currentYear);
    updateCalendarGrid();
}