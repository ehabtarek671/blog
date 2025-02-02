const userImage = document.getElementById('user-image');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

userImage.addEventListener('change', () => {
    const image = userImage.files[0];
    const newImage = new Image(500, 500);
    newImage.addEventListener('load', () => {
        canvas.width = newImage.width;
        canvas.height = newImage.height;

        context.drawImage(newImage, 0, 0);

        URL.revokeObjectURL(newImage.src);
    });
    newImage.src = URL.createObjectURL(image);
    canvas.style.display = 'block';
});