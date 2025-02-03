const API = '/login/';
const form = document.getElementById('login-form');

function getCSRFToken() {
    const csrfToken = document.cookie.split('; ').find((item) => item.startsWith('csrftoken=')).split('=')[1];
    return csrfToken;
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const csrfToken = getCSRFToken();

    fetch(API, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': `${csrfToken}`
        },
        body: JSON.stringify({
            email: `${formData.get('user_email')}`,
            pwd: `${formData.get('user_password')}`,
        })
    })
    .then(response => response.json())
    .then((data) => {
        if (data.message === 'Error') {

            const inputs = document.querySelectorAll('.input-field input');
            const errorBox = document.querySelector('.error-box');
            errorBox.setAttribute('id', 'visible');
            setTimeout(() => {
                errorBox.removeAttribute('id');
            }, 5000);
            inputs.forEach((input) => {
                input.classList.add('error');
            });

        } else if (data.message === 'Accepted') {

            window.location.replace('/');

        }
    })
    .catch(err => console.error(err));
});