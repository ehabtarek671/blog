const userImage = document.getElementById('user-image');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
 
userImage.addEventListener('change', () => {
    const image = userImage.files[0];
    const newImage = new Image();

    newImage.addEventListener('load', () => {
        const maxWidth = 500;
        const maxHeight = 500;

        let width = newImage.width;
        let height = newImage.height;
 
        if (width > maxWidth || height > maxHeight) {
            const scale = Math.min(maxWidth / width, maxHeight / height);
            width *= scale;
            height *= scale;
        }
 
        canvas.width = width;
        canvas.height = height;
 
        context.drawImage(newImage, 0, 0, width, height);
 
        URL.revokeObjectURL(newImage.src);
    });
 
    newImage.src = URL.createObjectURL(image);
    canvas.style.display = 'block';
});