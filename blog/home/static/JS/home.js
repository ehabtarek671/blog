const postsContainer = document.querySelector('.posts-container');
const API = '/api/blogs/';
const DELETEAPI = '/newblog/create/';

const fetchAPI = fetch(API)
.then(response => response.json())
.then((data) => {
    insertPosts(data)
})
.catch(err => console.error(err));

// Function to get the CSRF token from cookies
function getCSRFToken() {
    const csrfToken = document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
    
    return csrfToken;
}


function insertPosts(data) {
    for (let i = 0; i < data.posts.length; i++) {
        let post = document.createElement('div');
        post.classList.add('post');

        post.innerHTML =
        `
        <a href="/p/${data.posts[i].url}" class="title-link"><h2>${data.posts[i].title}</h2></a>
        <span>${data.posts[i].author}</span>
        <p>${data.posts[i].content}</p>
        <button id="${data.posts[i].url}" class="delete-button">Delete</button>
        `;
        postsContainer.append(post);
    }
}

document.addEventListener('click', (e) => {
    if (e.target.classList.contains('delete-button')) {
        const csrfToken  = getCSRFToken();
        let primaryKey = e.target.id;
        fetch(DELETEAPI, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': `${csrfToken}`
            },
            body: JSON.stringify({id: primaryKey})
        })
        .then(response => response.json())
        .then((data) => {
            console.log(`Delete post ${data.message}`);
            e.target.parentElement.remove();
        })
        .catch(err => console.error(err));
    }
});

/* ----------------------------------------------------------------------------- */

const nav = document.querySelector('header ul');
const userAPI = '/api/me/';

const fetchUser = fetch(userAPI)
.then(response => response.json())
.then((data) => {
    checkUser(data);
})
.catch(err => console.error(err));

function checkUser(data) {
    if (data.message === 'error') {
        nav.innerHTML = /* Html */
        `
        <li>
            <a href="/signup">
                <span>Sign Up</span>
            </a>
        </li>
        <li>
            <a href="/login">
                <span>Log In</span>
            </a>
        </li>
        `;
    } else if (data.name) {
        nav.innerHTML = /* Html */
        `
        <li>
            <a href="/create">
                <span>Create</span>
                <span class="material-symbols-outlined">add_circle</span>
            </a>
        </li>
        <li>
            <a href="#" id="profile-image-holder">
                <img src="${data.profileimage}" id="profile-image">
            </a>
        </li>
        `;
    }
}