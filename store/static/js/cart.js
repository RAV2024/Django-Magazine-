document.getElementById('clear-cart-button').addEventListener('click', function() {
       fetch('/clear-cart/', {
           method: 'POST',
           headers: {
               'X-CSRFToken': getCookie('csrftoken')
           }
       })
       .then(response => response.json())
       .then(data => {
           if (data.success) {
               document.querySelector('.cart-items').innerHTML = '';
               document.querySelector('.cart-summary').innerHTML = '<p>Ваша корзина пуста.</p>';
               document.querySelector('.cart-count').innerText = '0';
               alert('Корзина очищена!');
           } else {
               alert('Ошибка при очистке корзины.');
           }
       })
       .catch(error => console.error('Error:', error));
   });

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', function () {
    const decrementButtons = document.querySelectorAll('.decrement');
    const incrementButtons = document.querySelectorAll('.increment');

    decrementButtons.forEach(button => {
        button.addEventListener('click', function () {
            const itemId = this.dataset.itemId;
            updateCartItem(itemId, -1);
        });
    });

    incrementButtons.forEach(button => {
        button.addEventListener('click', function () {
            const itemId = this.dataset.itemId;
            updateCartItem(itemId, 1);
        });
    });

    function updateCartItem(itemId, change) {
        fetch(`/cart/update/${itemId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ change: change })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const quantityElement = document.querySelector(`.quantity[data-item-id="${itemId}"]`);
                const itemQuantityElement = document.querySelector(`.item-quantity[data-item-id="${itemId}"]`);
                const itemElement = document.querySelector(`.cart-item[data-item-id="${itemId}"]`);
                const totalAmountElement = document.querySelector('.total-amount');
                const cartCountElement = document.querySelector('.cart-count');

                let previousQuantity = parseInt(quantityElement.textContent);
                let newQuantity;

                if (change === -1) {
                    newQuantity = Math.max(0, previousQuantity - 1);
                } else if (change === 1) {
                    newQuantity = previousQuantity + 1;
                } else {
                    newQuantity = change;
                }

                if (newQuantity === 0) {
                    itemElement.remove();

                    if (document.querySelectorAll('.cart-item').length === 0) {
                        document.querySelector('.cart-container').innerHTML = '<p>Ваша корзина пуста.</p>';
                    }
                } else {
                    quantityElement.textContent = newQuantity;
                    if (itemQuantityElement) {
                        itemQuantityElement.textContent = newQuantity;
                    }
                }

                const totalItems = parseInt(data.cart_count);
                cartCountElement.textContent = totalItems;

                const total = parseFloat(data.total);
                if (!isNaN(total)) {
                    totalAmountElement.textContent = total.toFixed(0);
                } else {
                    console.error('Invalid total value from server:', data.total);
                }
            } else {
                alert('Ошибка при обновлении товара.');
            }
        })
        .catch(error => console.error('Ошибка:', error));
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

