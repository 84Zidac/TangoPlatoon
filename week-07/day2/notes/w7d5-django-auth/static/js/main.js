function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

axios.defaults.headers.common['X-CSRFToken'] = csrftoken

const signUp = (event) => {
    event.preventDefault();
    let email =  document.getElementById('email').value
    let name = document.getElementById('name').value
    let password = document.getElementById('password').value
    axios.post('/signup/', {
        email : email,
        name : name,
        password : password
    })
    .catch((err)=>{
        alert(err)
    })
    .then((response)=>{
        if (response.data.success !== false){
            window.location.href = '/sign_in/'
        }
        else{
            window.location.reload()
        }
    })
}

const signIn = (event) => {
    event.preventDefault();
    let email =  document.getElementById('email').value
    let password = document.getElementById('password').value
    axios.post('/signin/', {
        email : email,
        password : password
    })
    .catch((err)=>{
        alert(err)
    })
    .then((response)=>{
        if (response.data.signin !== false){
            window.location.href = '/tasks/'
        }
        else{
            window.location.reload()
        }
    })
}


const createTask = (event) => {
    event.preventDefault();
    let title = document.getElementById('title').value
    let description = document.getElementById('description').value

    axios.post('/tasks/', {
        title : title,
        description : description
    })
    .catch((err) => {
        alert(err)
    })
    .then((response)=>{
        if(response.data.success){
            window.location.reload()
        }
    })
}

const signOut = () => {
    axios.post('/signout/')
    .catch((err) => {
        alert(err)
    })
    .then((response)=>{
        if(response.data.signout){
            window.location.href = '/'
        }
    })
}