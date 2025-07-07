function login()
{
    // Get the username and password from the input fields
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Perform validation (this is a simple example, you might want to add more checks)
    if (username === "" || password === "")
    {
        alert("Please fill in both fields.");
        return;
    }

    try
    {
        fetch('/api/users/login', {
            method: 'POST',
            headers:{ 'Content-Type': 'application/json'},
            body: JSON.stringify({ username: username, password: password })
        }).then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log("Login successful");
                localStorage.setItem("token", data.token); // Store the token in local storage
                localStorage.setItem("username", username); // Store the username in local storage
                // Redirect to the main page or dashboard
                window.location.href = "dashboard.html";
            }
            else {
                console.error("Login failed:", data.message);
            }
        });
    }
    catch (error)
    {
        console.error("Error during login:", error);
    }
}