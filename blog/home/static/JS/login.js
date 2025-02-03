const API = '/login/';
const form = document.getElementById('login-form');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);

    const fetchAPI = fetch(API, {
        method: 'POST',
        headers: {
            "Content-Type": "multipart/form-data",
        }
    })
});