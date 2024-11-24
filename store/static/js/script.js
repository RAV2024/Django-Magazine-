function changeMainImage(selectedImage) {
    const mainImage = document.getElementById('main-image');
    mainImage.src = selectedImage.src;
}


function selectSize(button) {
    const buttons = document.querySelectorAll('.size-button');
    buttons.forEach(btn => btn.classList.remove('selected'));

    button.classList.add('selected');
     document.getElementById('add-to-cart').style.display = 'block';
}




