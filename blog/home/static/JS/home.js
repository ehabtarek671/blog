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
        <h2>${data[i].fields.title}</h2>
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
<<<<<<< HEAD
        fetch(DELETEAPI, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN': document.cookie.split('; ').at(3).split('=')[1]
=======
        fetch(API, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
>>>>>>> 70e6b47aa0d46eb5717f5decea141735540ea0bf
            },
            body: JSON.stringify({id: primaryKey})
        })
        .then(response => response.json())
<<<<<<< HEAD
        .then((data) => {
            console.log(data)
            e.target.parentElement.remove();
        })
        .catch(err => console.error(err));
    }
=======
        .then(data => console.log(data))
        .catch(err => console.error(err));
    }
>>>>>>> 70e6b47aa0d46eb5717f5decea141735540ea0bf
});