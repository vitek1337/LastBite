document.getElementById('open-login').addEventListener('click', function () {
  document.getElementById('login-modal').style.display = 'flex';
});

function closeModal(id) {
  document.getElementById(id).style.display = 'none';
}

function openProductModal(title, price) {
  document.getElementById('product-title').textContent = title;
  document.getElementById('product-price').textContent = price;
  document.getElementById('product-modal').style.display = 'flex';
}
