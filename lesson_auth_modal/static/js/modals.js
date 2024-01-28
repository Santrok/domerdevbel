const login_button = document.querySelector(".login_button");
const register_button = document.querySelector(".register_button");
const login_popup = document.querySelector(".popup_login");
const register_popup = document.querySelector(".popup_register");

login_button.addEventListener("click", () => {
    console.log('Johan');
    login_popup.style.display = 'flex';
    register_popup.style.display = 'none';
});


register_button.addEventListener("click", () => {
    register_popup.style.display = 'flex';
    login_popup.style.display = 'none';
});


const form_login_button = document.querySelector('#form_login_button')
const form_register_button = document.querySelector('#form_register_button')


form_login_button.addEventListener('click', login_fn)
form_register_button.addEventListener('click', register_fn)
let csrftoken = getCookie('csrftoken');

function login_fn(){
    console.log('Вход')
    fetch('http://127.0.0.1:8000/modal/data/', {
        method:"POST",
        headers: { "X-CSRFToken": csrftoken },
        body: JSON.stringify({'ussername':'johan'})
    }).then(response=>response.json())
        .then(data => {
            console.log(data);
            if (data.key === "1"){
                document.body.innerHTML+='<h1>Ты в личном кабинете</h1>'
            }
            else {
                document.body.innerHTML+='<h1>Все плохо</h1>'
            }
        })
}



function register_fn(){
    console.log("Регистрация")
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue
}