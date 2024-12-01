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





document.getElementById('add-to-cart-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const actionUrl = this.action;

    fetch(actionUrl, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.querySelector('.cart-count').innerText = data.cart_count;
            alert('Товар добавлен в корзину!');
        } else {
            if (data.error === 'not_authenticated') {
                alert('Вы не авторизованы. Пожалуйста, войдите в систему.');
                window.location.href = '/login';
            } else {
                alert(data.error);
            }
        }
    })
    .catch(error => console.error('Error:', error));
});



