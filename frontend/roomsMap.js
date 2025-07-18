    var rooms = [];

    function showRoomData(room) {
        document.getElementById('roomDataContent').style.display = 'block';
        document.getElementById('roomName').textContent = room.name;
        document.getElementById('roomCapacity').textContent = room.capacity;
        document.getElementById('roomDescription').textContent = room.description;
        document.getElementById("roomName").style.backgroundColor = room.color;
        roomImage = document.querySelector('#roomData img');
        roomImage.addEventListener("error",loadDefaultImage);
        roomImage.src = `assets/${room.id}.png`; // Reset to default image
    }

    function loadDefaultImage(event){
        event.target.error = null;
        event.target.src = "assets/roomimage.png";
    }

    function clearRoomData() {
        document.getElementById('roomDataContent').style.display = 'none';
        document.getElementById('roomName').textContent = '';
        document.getElementById('roomCapacity').textContent = '';
        document.getElementById('roomDescription').textContent = '';
        document.querySelector('#roomData img').src = ""; // Reset to default image
        document.getElementById("roomName").style.backgroundColor = "#FFFFFF";
    }

    function gotoRoomCalendar(roomId) {
        localStorage.setItem("roomId", roomId);
        window.location.href = `roomDetails.html`;
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