    var rooms = [];

    function showRoomData(room) {
        document.getElementById('roomName').textContent = room.name;
        document.getElementById('roomCapacity').textContent = room.capacity;
        document.getElementById('roomDescription').textContent = room.description;
        // Se quiser trocar a imagem, pode adicionar um campo image em room e trocar aqui
        // document.querySelector('#roomData img').src = room.image;
        //listar reservas da sala, se houver
        // let reservesList = room.reserves.map(reserve => 
        //     `<li>${reserve.user} - ${reserve.date} ${reserve.time}</li>`
        // ).join('');
        // if (reservesList) {
        //     document.getElementById('roomDescription').innerHTML += `<p>Reservas:</p><ul>${reservesList}</ul>`;
        // } else {
        //     document.getElementById('roomDescription').innerHTML += `<p>Não há reservas para esta sala.</p>`;
        // }
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
        fetch('http://localhost:5000/api/rooms/all')
        .then(response => response.json())
        .then((data) => {
                rooms = data;
                redrawRoomsMap();
            }
        ).catch(error => {console.error('Error fetching rooms:', error); rooms = [];});
    }

    function redrawRoomsMap()
    {
        if (!rooms) return;
        if (rooms.length == 0) return;

        let svg = document.getElementById('roomSvg');
        svg.innerHTML = ''; // Clear previous polygons
        console.log(rooms);

        for (let i = 0; i < rooms.length; i++) {
            let room = rooms[i];
            
            if(room.location === "") continue;

            let points = room.location;
            console.log(`Room ${i}: ${points}`); // Log the points for debugging
            let polygon = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
            polygon.setAttribute('points', points);
            polygon.setAttribute('data-room-id', room.id);
            polygon.style.cursor = "pointer";
            polygon.style.pointerEvents = "all";
            
            console.log(`roomData: ${room.name}, ${room.description}`);
            polygon.addEventListener('mouseenter', () => showRoomData(room));
            polygon.addEventListener('mouseleave', clearRoomData);
            polygon.addEventListener('click', () => gotoRoomCalendar(room.id));

            svg.appendChild(polygon);
        }
    }