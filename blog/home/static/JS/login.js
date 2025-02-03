const API = '/login/';
const form = document.getElementById('login-form');

form.addEventListener('submit', (e) => {
    const formData = new FormData(form);

    fetch(API, {
        method: 'POST',
        headers: {
            'Content-Type': 'multipart/form-data',
        },
        body: formData,
    })
    .then(response => response.json())
    .then((data) => {
        if (data.message === 'Error') {
            e.preventDefault();
            console.log('Error, Credentials you entered are wrong');
        } else if (data.message === 'Accepted') {
            window.location.replace('/');
        }
    })
    .catch(err => console.error(err));
});