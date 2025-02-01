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
        let postl = document.createElement('div');
        postl.classList.add('post');

        postl.innerHTML =
        `
        <a href="/p/${data.posts[i].url}" class="title-link"><h2>${data.posts[i].title}</h2></a>
        <span>${data.posts[i].author.name}</span>
        <p>${data.posts[i].content}</p>
        <button id="${data.posts[i].url}" class="delete-button">Delete</button>
        `;
        postsContainer.append(postl);
    }
}

document.addEventListener('click', (e) => {
    if (e.target.classList.contains('delete-button')) {
        const csrfToken  = getCSRFToken()
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
            console.log(data);
            e.target.parentElement.remove();
        })
        .catch(err => err);
    }
});