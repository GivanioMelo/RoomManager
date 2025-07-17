const JAN = 0;
const FEB = 1;
const MAR = 2;
const APR = 3;
const MAY = 4;
const JUN = 5;
const JUL = 6;
const AUG = 7;
const SEP = 8;
const OCT = 9;
const NOV = 10;
const DEZ = 11;

const MonthNames = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho","Agosto","Setembro", "Outubro","Novembro", "Dezembro"];

reserves = [
    {user:'Alice', month:JUL, day: 9, startTime: "08:00", endTime: "12:00" },
    {user:'Dave', month:JUL, day: 9, startTime: "18:00", endTime: "22:00" },
];

function pageLoad() {
    let today = new Date();

    localStorage.setItem('currentMonth',today.getMonth());
    localStorage.setItem('currentYear',today.getFullYear());

    let roomId = localStorage.getItem("roomId");
    if (!roomId) {window.location.href = "roomsMap.html"; return;}
    
    updateCalendarGrid();
}

function openDayProgram(day, month) {
    let roomId = localStorage.getItem("roomId");
    if (!roomId) {window.location.href = "roomsMap.html"; return;}
    let selectedDate = new Date(new Date().getFullYear(), month, day);
    localStorage.setItem("selectedDate", selectedDate.toISOString().split('T')[0]); // Store date in YYYY-MM-DD format
    window.location.href = "day.html";
}

function updateCalendarGrid() {
    const calendarGrid = document.getElementById('calendarGrid');
    calendarGrid.innerHTML = ''; // Clear previous content
    let rowOffset = 0;
    
    let currentMonth = parseInt(localStorage.getItem('currentMonth')); // Months are 0-indexed
    let currentYear = parseInt(localStorage.getItem('currentYear'));

    document.getElementById('currentMonthDisplay').textContent = new Date(currentYear, currentMonth).toLocaleString('default', { month: 'long' }) + ' ' + currentYear;
    rowsStart = 2; // Start from the second row for the days
    for (let i = 1; i < 32; i++) {    
        const date = new Date(currentYear, currentMonth, i);
        const weekday = date.getDay();

        if (date.getMonth() > (currentMonth)) continue; // Skip days that are not in the current month

        console.log("Date: " + date.toDateString() + ", Weekday: " + weekday);

        const dayCell = document.createElement('div');
        dayCell.className = 'day-cell';
        dayCell.style.gridColumnStart = weekday + 1; // Adjust for CSS grid
        dayCell.style.gridRowStart = rowsStart;
        if (weekday == 6) rowsStart++; // Move to the next row after Saturday
        dayCell.textContent = i; // Placeholder for day numbers

        for (const reserve of reserves) {
            if (reserve.month === currentMonth && reserve.day === i) {
                const reserveBox = document.createElement('div');
                reserveBox.className = 'reserve';
                reserveBox.textContent = `${reserve.user} ${reserve.startTime} - ${reserve.endTime}`;
                reserveBox.style.gridRowStart = rowsStart;
                reserveBox.style.gridColumnStart = weekday + 1;
                reserveBox.style.gridColumnEnd = weekday + 2; // Span one column
                reserveBox.style.position = 'relative';
                reserveBox.style.zIndex = '2'; // Ensure it floats above day cell
                dayCell.appendChild(reserveBox);
            }
        }

        calendarGrid.appendChild(dayCell);
    }
}

function nextMonth() {
    let currentMonth = parseInt(localStorage.getItem('currentMonth')); // Months are 0-indexed
    let currentYear = parseInt(localStorage.getItem('currentYear'));

    if (currentMonth === DEZ) { currentMonth = JAN; currentYear += 1; }
    else { currentMonth += 1; }

    localStorage.setItem('currentMonth', currentMonth);
    localStorage.setItem('currentYear', currentYear);
    updateCalendarGrid();
}

function previousMonth() {
    let currentMonth = parseInt(localStorage.getItem('currentMonth')); // Months are 0-indexed
    let currentYear = parseInt(localStorage.getItem('currentYear'));

    if (currentMonth === JAN) { currentMonth = DEZ; currentYear -= 1; }
    else { currentMonth -= 1; }

    localStorage.setItem('currentMonth', currentMonth);
    localStorage.setItem('currentYear', currentYear);
    updateCalendarGrid();
}