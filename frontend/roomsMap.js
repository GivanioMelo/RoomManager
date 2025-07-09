        const rooms = [
            {
                id: 0, name: "Conference Room",
                capacity: 10,
                description: "A spacious conference room with a projector.",
                location:"312,449 338,477 418,411 389,379",
                reserves: [
                    {id: 1, user: "Alice", date: "2023-10-01", time: "10:00-11:00"},
                    {id: 2, user: "Bob", date: "2023-10-02", time: "14:00-15:00"}
                ]
            },
            {   id: 1,
                name: "Meeting Room",
                capacity: 5,
                description: "A small meeting room for team discussions.",
                location:"351,338 392,382 310,452 262,404",
                reserves: [
                    {id: 3, user: "Charlie", date: "2023-10-03", time: "09:00-10:00"},
                    {id: 4, user: "Diana", date: "2023-10-04", time: "11:00-12:00"}
                ]
            },
            {   id: 2,
                name: "Training Room",
                capacity: 20,
                description: "A large room for training sessions.",
                location:"339,212 226,134 332,37 410,146",
                reserves: []
            },
        ];

    function showRoomData(room) {
        document.getElementById('roomName').textContent = room.name;
        document.getElementById('roomCapacity').textContent = room.capacity;
        document.getElementById('roomDescription').textContent = room.description;
        // Se quiser trocar a imagem, pode adicionar um campo image em room e trocar aqui
        // document.querySelector('#roomData img').src = room.image;
        //listar reservas da sala, se houver
        let reservesList = room.reserves.map(reserve => 
            `<li>${reserve.user} - ${reserve.date} ${reserve.time}</li>`
        ).join('');
        if (reservesList) {
            document.getElementById('roomDescription').innerHTML += `<p>Reservas:</p><ul>${reservesList}</ul>`;
        } else {
            document.getElementById('roomDescription').innerHTML += `<p>Não há reservas para esta sala.</p>`;
        }
    }

    function clearRoomData() {
        document.getElementById('roomName').textContent = '';
        document.getElementById('roomCapacity').textContent = '';
        document.getElementById('roomDescription').textContent = '';
        // document.querySelector('#roomData img').src = 'assets/roomimage.png'; // Reset to default image
    }

    function gotoRoomCalendar(roomId) {
        localStorage.setItem("roomId", roomId);
        window.location.href = "calendar.html";
    }

    function pageLoad() {
        let svg = document.getElementById('roomSvg');
        svg.innerHTML = ''; // Clear previous polygons

        rooms.forEach((room, idx) => {
            let points = room.location;
            console.log(`Room ${idx}: ${points}`); // Log the points for debugging
            let polygon = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
            polygon.setAttribute('points', points);
            polygon.setAttribute('data-room-id', room.id);
            polygon.style.cursor = "pointer";
            polygon.style.pointerEvents = "all";
            
            polygon.addEventListener('mouseenter', () => showRoomData(room));
            polygon.addEventListener('mouseleave', clearRoomData);
            polygon.addEventListener('click', () => gotoRoomCalendar(room.id));

            svg.appendChild(polygon);
        });
    }