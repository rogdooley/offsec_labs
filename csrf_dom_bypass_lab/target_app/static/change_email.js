// Token is pulled from the hash fragment (vulnerable)
const token = location.hash.split('csrf=')[1];

document.getElementById("submit-btn").addEventListener("click", () => {
    const newEmail = document.getElementById("email").value;
    fetch("/api/update-email", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRF-Token": token
        },
        body: JSON.stringify({ email: newEmail })
    })
    .then(res => res.json())
    .then(json => alert("Email updated to: " + json.new))
    .catch(err => alert("Error: " + err));
});
