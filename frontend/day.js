reserves = [
    { startTime: 8, endTime: 12 },
    { startTime: 18, endTime: 22 }
];

function pageLoad() {
    let year = localStorage.getItem('currentYear');
    let month = localStorage.getItem('currentMonth');
    let day = localStorage.getItem('selectedDay');
    
    let selectedDate = Date(year,month,day);

    let roomId = localStorage.getItem("roomId");

    document.getElementById("dateHeader").innerHTML = selectedDate.toLocaleString();
    // fetch(`http://localhost:5000/api/reserves/getByRoomAndDate?roomId=${roomId}&date=${year}-${month+1}-${day}`)
    // .then(response => response.json())
    // .then((data) => {
    //     reserves = data;
    // })
    // .catch();

    updateDayProgramGrid();
}

function updateDayProgramGrid() {
    const dayProgramGrid = document.getElementById("DayProgramGrid");
    dayProgramGrid.innerHTML = "";

    for (let i = 7; i <= 22; i++) {
        const timeSlot = document.createElement("div");
        timeSlot.className = "timeSlot";
        timeSlot.textContent = `${i}:00`;
        timeSlot.style.gridRowStart = i - 6 + 1; // Corrected: grid rows start at 1
        timeSlot.style.gridRowEnd = i - 6 + 2; // Corrected: end is exclusive
        timeSlot.style.gridColumn = "1"; // Span all columns
        dayProgramGrid.appendChild(timeSlot);
        console.log(`Time slot added: ${i}:00 at position `+ (i - 6));
    }

    for (const reserve of reserves)
    {
        const reserveBox = document.createElement("div");
        reserveBox.className = "reserve";
        reserveBox.textContent = `${reserve.startTime} - ${reserve.endTime}`;
        reserveBox.style.gridRowStart = reserve.startTime - 6 + 1; // Corrected: grid rows start at 1
        reserveBox.style.gridRowEnd = reserve.endTime - 6 + 2; // Corrected: end is exclusive
        reserveBox.style.gridColumn = "1 / -1"; // Span all columns
        reserveBox.style.position = "relative";
        reserveBox.style.zIndex = "2"; // Ensure it floats above timeslots
        console.log(`Reserve box added: ${reserve.startTime} - ${reserve.endTime} at row start ` + (reserve.startTime - 6 + 1) + " and row end " + (reserve.endTime - 6 + 2));
        dayProgramGrid.appendChild(reserveBox);
    }
}