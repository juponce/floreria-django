var actualizarBtns = document.getElementsByClassName('actualizar-carrito');

var updateBtn = document.getElementsByClassName('update-cart');

for (i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        var user = this.dataset.user;
        console.log('idProducto: ', productId, 'Action:', action);

        console.log('USER:', user);

        if (user === 'AnonymousUser') {
            console.log('Usuario no registrado');
        } else {
            updateUserOrderOnCart(productId, action);
        }
    });
}

for (i = 0; i < actualizarBtns.length; i++) {
    actualizarBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        var user = this.dataset.user;
        console.log('idProducto: ', productId, 'Action:', action, 'User: ', user);

        console.log('USER:', user);

        if (user === 'AnonymousUser') {
            console.log('Usuario no registrado');
        } else {
            updateUserOrder(productId, action);
        }
    });
}

function updateUserOrder(productId, action) {
    console.log('User is logged in, sending data...');

    var url = 'agregar_producto/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action }),
    })
        .then((response) => {
            return response.json();
        })

        .then((data) => {
            console.log('data:', data);
            location.reload();
        });
}

function updateUserOrderOnCart(productId, action) {
    console.log('User is logged in, sending data...');

    var url = '../agregar_producto/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action }),
    })
        .then((response) => {
            return response.json();
        })

        .then((data) => {
            console.log('data:', data);
            location.reload();
        });
}


var comprarBtn = document.getElementsByClassName('confirmar-compra');

for (i = 0; i < comprarBtn.length; i++) {
    comprarBtn[i].addEventListener('click', function () {
        var carritoId = this.dataset.id;
        var action = this.dataset.action;
        var total = this.dataset.total;
        console.log('carritoId: ', carritoId, 'Action:', action, 'Total', total);

        console.log('USER:', user);

        if (user === 'AnonymousUser') {
            console.log('Usuario no registrado');
        } else {
            setPedido(carritoId, action, total);
        }
    });
}

function setPedido(carritoId, action, total) {
    console.log('User is logged in, sending data...');

    var url = '../comprar/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'carritoId': carritoId, 'action': action, 'total': total}),
    })
        .then((response) => {
            return response.json();
        })

        .then((data) => {
            console.log('data:', data);
            location.href = '/?success';
        });
}