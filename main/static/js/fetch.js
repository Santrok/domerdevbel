let data = document.querySelector('.data')

function fn() {
    fetch('http://127.0.0.1:8000/adver/')
        .then(resp => resp.json())
        .then(data => {
            console.log(data);
        })

}

fn()