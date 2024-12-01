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
    const quantityInputs = document.querySelectorAll('.quantity');

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

    quantityInputs.forEach(input => {
        input.addEventListener('change', function () {
            const itemId = this.dataset.itemId;
            const newQuantity = parseInt(this.value);
            if (newQuantity > 0) {
                updateCartItem(itemId, newQuantity); // передаем новый объем
            } else {
                alert("Количество не может быть меньше 1.");
                location.reload(); // Или можете очистить поле
            }
        });
    });

    function updateCartItem(itemId, change) {
        fetch(`/cart/update/${itemId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ change: change })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const itemQuantityElement = document.querySelector(`.item-quantity[data-item-id="${itemId}"]`);
                const quantityInput = document.querySelector(`.quantity[data-item-id="${itemId}"]`);
                const totalAmountElement = document.querySelector('.total-amount');

                let previousQuantity = parseInt(quantityInput.value);
                let newQuantity;

                if (change === -1) {
                    newQuantity = Math.max(0, previousQuantity - 1);
                } else if (change === 1) {
                    newQuantity = previousQuantity + 1;
                } else {
                    newQuantity = change;
                }

                quantityInput.value = newQuantity;
                itemQuantityElement.textContent = newQuantity;

                const itemPriceText = itemQuantityElement.closest('.cart-item-info').querySelector('p:nth-child(4)').innerText;
                const itemPrice = parseFloat(itemPriceText.replace(' руб.', '').replace(/s/g, ''));
                const currentTotalText = totalAmountElement.innerText;
                const currentTotal = parseFloat(currentTotalText.replace(' руб.', '').replace(/s/g, ''));

                // Проверка валидности
                if (isNaN(itemPrice) || isNaN(currentTotal)) {
                    console.error('Некорректные значения:', itemPrice, currentTotal);
                    return; // Прекращаем выполнение
                }

                const newTotal = currentTotal + (newQuantity - previousQuantity) * itemPrice;

                totalAmountElement.textContent = newTotal.toFixed(0) + ' руб.';
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