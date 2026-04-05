// Cart Page Script
document.addEventListener("DOMContentLoaded", function () {
  renderCart();
  setupCartEventListeners();
  updateCartCount();
});

function setupCartEventListeners() {
  const checkoutBtn = document.getElementById("checkoutBtn");
  if (checkoutBtn) {
    checkoutBtn.addEventListener("click", handleCheckout);
  }

  // Delegate quantity changes and remove buttons
  const cartItems = document.getElementById("cartItems");
  if (cartItems) {
    cartItems.addEventListener("click", handleCartAction);
    cartItems.addEventListener("change", handleQuantityChange);
  }
}

function renderCart() {
  const cart = getCartFromStorage();
  const cartItemsEl = document.getElementById("cartItems");
  const emptyCartEl = document.getElementById("emptyCart");
  const checkoutBtn = document.getElementById("checkoutBtn");

  if (cart.length === 0) {
    cartItemsEl.innerHTML = "";
    emptyCartEl.classList.remove("hidden");
    if (checkoutBtn) checkoutBtn.style.display = "none";
    updateCartSummary([]);
    return;
  }

  emptyCartEl.classList.add("hidden");
  if (checkoutBtn) checkoutBtn.style.display = "block";

  cartItemsEl.innerHTML = cart
    .map((cartItem) => {
      const product = getProduct(cartItem.id);
      if (!product) return "";

      const itemTotal = product.price * cartItem.quantity;

      return `
            <div class="cart-item" data-id="${product.id}">
                <div class="item-image">
                    <img 
                        src="${product.image}" 
                        alt="${product.name}"
                        title="${product.name}"
                        class="item-photo"
                        loading="lazy"
                        decoding="async"
                        onerror="this.src='https://via.placeholder.com/100?text=${encodeURIComponent(product.name)}'"
                    />
                </div>
                
                <div class="item-details">
                    <h3>${product.name}</h3>
                    <p class="item-price">${formatPrice(product.price)} per item</p>
                    <p class="item-stock">Stok tersedia: ${product.stock}</p>
                </div>
                
                <div class="item-quantity">
                    <label for="qty-${product.id}">Qty:</label>
                    <input 
                        type="number" 
                        id="qty-${product.id}"
                        class="qty-input" 
                        data-id="${product.id}"
                        value="${cartItem.quantity}" 
                        min="1" 
                        max="${product.stock}"
                    >
                </div>
                
                <div class="item-total">
                    <span class="total-price">${formatPrice(itemTotal)}</span>
                </div>
                
                <button 
                    class="btn-remove" 
                    data-id="${product.id}"
                    title="Hapus dari keranjang"
                >
                    ✕
                </button>
            </div>
        `;
    })
    .join("");

  updateCartSummary(cart);
}

function handleQuantityChange(e) {
  if (e.target.classList.contains("qty-input")) {
    const productId = parseInt(e.target.dataset.id);
    const newQuantity = parseInt(e.target.value);
    const product = getProduct(productId);

    if (newQuantity > product.stock) {
      e.target.value = product.stock;
      alert(`Maaf, stok hanya tersedia ${product.stock}`);
      updateCartQuantity(productId, product.stock);
    } else {
      updateCartQuantity(productId, newQuantity);
    }

    renderCart();
  }
}

function handleCartAction(e) {
  if (e.target.classList.contains("btn-remove")) {
    const productId = parseInt(e.target.dataset.id);
    const product = getProduct(productId);

    if (confirm(`Hapus "${product.name}" dari keranjang?`)) {
      removeFromCart(productId);
      renderCart();
    }
  }
}

function updateCartSummary(cart) {
  let subtotal = 0;

  cart.forEach((item) => {
    const product = getProduct(item.id);
    if (product) {
      subtotal += product.price * item.quantity;
    }
  });

  const shipping = subtotal > 0 ? 50000 : 0; // Free shipping for orders > 500k
  const tax = Math.floor(subtotal * 0.1); // 10% tax
  const total = subtotal + shipping + tax;

  // Update display
  document.getElementById("subtotal").textContent = formatPrice(subtotal);
  document.getElementById("shipping").textContent = formatPrice(shipping);
  document.getElementById("tax").textContent = formatPrice(tax);
  document.getElementById("total").textContent = formatPrice(total);
}

function handleCheckout() {
  const cart = getCartFromStorage();

  if (cart.length === 0) {
    alert("Keranjang Anda kosong");
    return;
  }

  // Calculate total
  let subtotal = 0;
  cart.forEach((item) => {
    const product = getProduct(item.id);
    if (product) {
      subtotal += product.price * item.quantity;
    }
  });

  const tax = Math.floor(subtotal * 0.1);
  const total = subtotal + 50000 + tax;

  // Show confirmation
  const message = `
Total belanja Anda: ${formatPrice(total)}

Apakah Anda ingin melanjutkan ke pembayaran?
    `;

  if (confirm(message)) {
    // Clear cart after "checkout"
    localStorage.removeItem("cart");
    alert("Terima kasih! Pesanan Anda sedang diproses.");
    renderCart();
    updateCartCount();
  }
}
