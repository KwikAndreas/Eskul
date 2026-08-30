// Initialize app
document.addEventListener("DOMContentLoaded", function () {
  updateCartCount();
  renderProducts(PRODUCTS);
  setupEventListeners();
});

// Setup Event Listeners
function setupEventListeners() {
  // Category filter
  const categoryFilter = document.getElementById("categoryFilter");
  if (categoryFilter) {
    categoryFilter.addEventListener("change", filterAndSort);
  }

  // Sort
  const sortBy = document.getElementById("sortBy");
  if (sortBy) {
    sortBy.addEventListener("change", filterAndSort);
  }

  // Search
  const searchBox = document.getElementById("searchBox");
  if (searchBox) {
    searchBox.addEventListener("input", handleSearch);
  }

  // Delegate click events for add to cart buttons
  const productsGrid = document.getElementById("productsGrid");
  if (productsGrid) {
    productsGrid.addEventListener("click", handleProductAction);
  }
}

// Handle Search
function handleSearch(e) {
  const searchTerm = e.target.value.toLowerCase();

  if (searchTerm === "") {
    renderProducts(PRODUCTS);
  } else {
    const filtered = PRODUCTS.filter(
      (product) =>
        product.name.toLowerCase().includes(searchTerm) ||
        product.description.toLowerCase().includes(searchTerm),
    );
    renderProducts(filtered);
  }
}

// Filter and Sort
function filterAndSort() {
  const category = document.getElementById("categoryFilter").value;
  const sortBy = document.getElementById("sortBy").value;

  let filtered = PRODUCTS;

  // Filter by category
  if (category) {
    filtered = filtered.filter((p) => p.category === category);
  }

  // Sort
  filtered = sortProducts(filtered, sortBy);

  renderProducts(filtered);
}

// Sort Products
function sortProducts(products, sortBy) {
  const sorted = [...products];

  switch (sortBy) {
    case "price-low":
      sorted.sort((a, b) => a.price - b.price);
      break;
    case "price-high":
      sorted.sort((a, b) => b.price - a.price);
      break;
    case "rating":
      sorted.sort((a, b) => b.rating - a.rating);
      break;
    default:
      // Terbaru (default order)
      break;
  }

  return sorted;
}

// Render Products
function renderProducts(products) {
  const grid = document.getElementById("productsGrid");
  const emptyState = document.getElementById("emptyState");

  if (!products.length) {
    grid.innerHTML = "";
    emptyState.classList.remove("hidden");
    return;
  }

  emptyState.classList.add("hidden");

  grid.innerHTML = products
    .map(
      (product) => `
        <article class="product-card" data-id="${product.id}">
            <div class="product-image">
                <img 
                    src="${product.image}" 
                    alt="${product.name}"
                    title="${product.name}"
                    class="product-photo"
                    loading="lazy"
                    decoding="async"
                    onerror="this.src='https://via.placeholder.com/280x210?text=${encodeURIComponent(product.name)}'"
                />
                ${product.stock < 5 ? '<span class="stock-warning">⚠️ Stok Terbatas</span>' : ""}
            </div>
            
            <div class="product-info">
                <h3 class="product-name">${product.name}</h3>
                
                <div class="product-rating">
                    <span class="stars">${"⭐".repeat(Math.floor(product.rating))}</span>
                    <span class="rating-value">${product.rating}</span>
                </div>
                
                <p class="product-description">${product.description}</p>
                
                <div class="product-footer">
                    <span class="product-price">${formatPrice(product.price)}</span>
                    <span class="product-stock">Stok: ${product.stock}</span>
                </div>
                
                <button 
                    class="btn btn-add-cart" 
                    data-id="${product.id}"
                    ${product.stock === 0 ? "disabled" : ""}
                >
                    ${product.stock === 0 ? "Stok Habis" : "+ Keranjang"}
                </button>
            </div>
        </article>
    `,
    )
    .join("");
}

// Handle Product Actions
function handleProductAction(e) {
  if (e.target.classList.contains("btn-add-cart")) {
    const productId = parseInt(e.target.dataset.id);
    const product = getProduct(productId);

    if (product && product.stock > 0) {
      addToCart(productId, 1);

      // Show feedback
      e.target.textContent = "✓ Ditambahkan";
      e.target.classList.add("added");

      setTimeout(() => {
        e.target.textContent = "+ Keranjang";
        e.target.classList.remove("added");
      }, 1500);
    }
  }
}
