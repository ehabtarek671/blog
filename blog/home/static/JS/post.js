const like = document.getElementById('like');
const dislike = document.getElementById('dislike');
const read = document.getElementById('read');
const preferences = document.querySelector('.preferences');

preferences.addEventListener('click', (e) => {
    if (e.target === like) {
        if (dislike.classList.contains('active')) {
            dislike.classList.remove('active');
        }
        like.classList.toggle('active');
    } else if (e.target === dislike) {
        if (like.classList.contains('active')) {
            like.classList.remove('active');
        }
        dislike.classList.toggle('active');
    } else if (e.target === read) {
        read.classList.toggle('active');
    }
});