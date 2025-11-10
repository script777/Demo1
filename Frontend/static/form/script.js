const form = document.getElementById("register_form_user");
const error_message = document.getElementById("error_message");

form.addEventListener("submit", async (e) =>{
    e.preventDefault();

    const data = {
        user_name: form.firstname.value,
        user_password: form.password.value,
    }
    try {
        const response = await fetch("http://localhost:8000/form", {
        method: "POST",
        headers: {"Content-Type": "aplication/json"},
        body: JSON.stringify(data)
    })

    const result = await response.json();
    console.log(result);
    
    
    } catch (error) {
        console.log("El error fue: ", error);
        error_message.innerText = "Ha ocurrido un error";
    }

    

})