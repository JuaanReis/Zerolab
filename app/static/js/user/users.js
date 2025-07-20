const userData = JSON.parse(localStorage.getItem("userData"))

if (userData) {
    document.getElementById("name").textContent = `Name: ${userData.user}`;
    document.getElementById("msg").textContent = `Mesage: ${userData.msg}`;
} else {
    document.getElementById("error").textContent = "No data received";
}