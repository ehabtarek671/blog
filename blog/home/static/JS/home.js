const postsContainer = document.querySelector('.posts-container');
const API = '/api/blogs/';

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
        <button id="${data[i].pk}">Delete</button>
        `;
        postsContainer.append(post);
    }
}

document.addEventListener("click", function(){
    
})