const images = document.querySelectorAll('.image-portfolio');

function handleImgOver() {
    const img = this.querySelector('img');
    const overlay = this.querySelector('.overlay');

    img.classList.add('img-hover');
    overlay.classList.add('overlay-hover');

}

function handleImgLeave() {
    const img = this.querySelector('img');
    const overlay = this.querySelector('.overlay');

    overlay.classList.remove('overlay-hover');
    img.classList.remove('img-hover');
}



images.forEach(image => image.addEventListener('mouseover', handleImgOver));
images.forEach(image => image.addEventListener('mouseleave', handleImgLeave));