const postsContainer = document.querySelector('.posts-container');
const API = '/api/blogs/';
const DELETEAPI = '/newblog/create/'
const fetchAPI = fetch(API)
.then(response => response.json())
.then((data) => {
    insertPosts(data);
})
.catch(err => console.error(err));

function insertPosts(data) {
    for (let i = 0; i < data.length; i++) {
        let post = document.createElement('div');
        post.classList.add('post');

        post.innerHTML =
        `
        <a href=/p/${data[i].pk} class="title-link"><h2>${data[i].fields.title}</h2></a>
        <span>${data[i].fields.author}</span>
        <p>${data[i].fields.content}</p>
        <button id="${data[i].pk}" class="delete-button">Delete</button>
        `;
        postsContainer.append(post);
    }
}

document.addEventListener('click', (e) => {
    if (e.target.classList.contains('delete-button')) {
        let primaryKey = e.target.id;
        fetch(DELETEAPI, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRF-Token': `${document.cookie.split('=')[1]}`,
            },
            body: JSON.stringify({id: primaryKey})
        })
        .then(response => response.json())
        .then((data) => {
            console.log(data);
            e.target.parentElement.remove();
        })
        .catch(err => console.error(err));
    }
});