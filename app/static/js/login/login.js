document.getElementById("form-id").addEventListener("submit", async (e) => {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch("/users", {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (!response.ok) {
            alert("Erro ao enviar dados");
            return;
        }

        window.location.href = "/users";

    } catch (err) {
        alert("Erro na requisição");
        console.error(err);
    }
});
