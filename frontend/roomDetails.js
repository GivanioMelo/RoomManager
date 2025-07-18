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

const WeekDayNames = ["Dom","Seg","Ter","Qua","Qui","Sex","Sab"];
const MonthNames = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho","Agosto","Setembro", "Outubro","Novembro", "Dezembro"];

var reserves = [
    {user:'Alice', month:JUL, day: 3, startTime: "08:00", endTime: "12:00" },
    {user:'Alice', month:JUL, day: 9, startTime: "08:00", endTime: "12:00" },
    {user:'Alice', month:JUL, day: 15, startTime: "08:00", endTime: "12:00" },
    {user:'Alice', month:JUL, day: 23, startTime: "08:00", endTime: "12:00" },
    {user:'Alice', month:JUL, day: 29, startTime: "08:00", endTime: "12:00" },
    {user:'Dave', month:JUL, day: 9, startTime: "18:00", endTime: "22:00" },
    {user:'Dave', month:JUL, day: 15, startTime: "18:00", endTime: "22:00" },
    {user:'Dave', month:JUL, day: 23, startTime: "18:00", endTime: "22:00" },
    {user:'Dave', month:JUL, day: 29, startTime: "18:00", endTime: "22:00" },
    {user:'Dave', month:JUL, day: 3, startTime: "18:00", endTime: "22:00" },
    {user:'Luiz', month:JUL, day: 3, startTime: "13:00", endTime: "17:00" },
    {user:'Luiz', month:JUL, day: 9, startTime: "13:00", endTime: "17:00" },
    {user:'Luiz', month:JUL, day: 15, startTime: "13:00", endTime: "17:00" },
    {user:'Luiz', month:JUL, day: 23, startTime: "13:00", endTime: "17:00" },
    {user:'Luiz', month:JUL, day: 29, startTime: "13:00", endTime: "17:00" },
];

function pageLoad() {
    let today = new Date();

    localStorage.setItem('currentMonth',today.getMonth());
    localStorage.setItem('currentYear',today.getFullYear());    

    let roomId = localStorage.getItem("roomId");
    if (!roomId) {window.location.href = "roomsMap.html"; return;}

    updateCalendarGrid();
}

function openDayProgram(day)
{
    let roomId = localStorage.getItem("roomId");
    if (!roomId) {window.location.href = "roomsMap.html"; return;}
    
    localStorage.setItem("selectedDay",day);
    month = localStorage.getItem("currentMonth");
    year = localStorage.getItem("currentYear");
    let selectedDate = new Date(new Date().getFullYear(), month, day);
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

    for(let i = 0; i<7; i++)
    {
        let weekHeader = document.createElement("div");
        weekHeader.textContent = WeekDayNames[i];
        weekHeader.className = "WeekDayHeader";
        weekHeader.style.gridRowStart = 1;
        weekHeader.style.gridColumnStart = i+1;
        calendarGrid.append(weekHeader);
    }

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
        dayCell.addEventListener("click",()=>openDayProgram(i));

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