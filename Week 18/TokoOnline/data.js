// Product Database
const PRODUCTS = [
  {
    id: 1,
    name: "iPhone 15 Pro",
    category: "smartphone",
    price: 12999000,
    stock: 15,
    rating: 4.8,
    image:
      "https://cdnpro.eraspace.com/media/catalog/product/a/p/apple_iphone_15_pro_natural_titanium_1a_4.jpg",
    description: "Smartphone flagship terbaru dengan prosesor A17 Pro",
  },
  {
    id: 2,
    name: "Samsung Galaxy S24",
    category: "smartphone",
    price: 10999000,
    stock: 22,
    rating: 4.7,
    image:
      "https://images.samsung.com/is/image/samsung/assets/id/offer/2024/9/galaxy-s24-fe/S24_FE_Color_Selection_Blue_MO.jpg?imbypass=true",
    description: "Samsung terbaru dengan AI features canggih",
  },
  {
    id: 3,
    name: 'MacBook Pro 14"',
    category: "laptop",
    price: 24999000,
    stock: 8,
    rating: 4.9,
    image:
      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpWBZ7n0-jkPwVfKjqIVUcM6DTu_vhJrTurw&s",
    description: "Laptop profesional dengan chip M3 Max",
  },
  {
    id: 4,
    name: "Dell XPS 15",
    category: "laptop",
    price: 18999000,
    stock: 12,
    rating: 4.6,
    image:
      "https://www.jktgadget.com/wp-content/uploads/2023/07/DELL-XPS-15-9530-1.jpg",
    description: "Laptop gaming & desain dengan RTX 4060",
  },
  {
    id: 5,
    name: "AirPods Pro Max",
    category: "aksesori",
    price: 7999000,
    stock: 30,
    rating: 4.5,
    image: "https://cdnpro.eraspace.com/media/catalog/product/a/p/apple_airpods_max_usb-c_midnight_1.jpg",
    description: "Headphone premium dengan noise cancellation",
  },
  {
    id: 6,
    name: "Smart Watch Ultra",
    category: "aksesori",
    price: 4499000,
    stock: 25,
    rating: 4.4,
    image:
      "https://images.samsung.com/is/image/samsung/p6pim/id/sm-l700ndaaxse/gallery/id-galaxy-watch-ultra-l705-529940-sm-l700ndaaxse-545254734?$Q90_1248_936_F_PNG$",
    description: "Smartwatch dengan durabilitas ekstrem",
  },
  {
    id: 7,
    name: "iPad Air",
    category: "aksesori",
    price: 9999000,
    stock: 18,
    rating: 4.7,
    image: "https://www.hellostore.id/cdn/shop/files/11_inci_01_1f7f5b14-4e20-4488-8142-6fd10e2dd8e7.jpg?v=1756579941&width=246",
    description: "Tablet powerful untuk kreativitas dan produktivitas",
  },
  {
    id: 8,
    name: "Google Pixel 8",
    category: "smartphone",
    price: 9299000,
    stock: 20,
    rating: 4.6,
    image:
      "https://discountstore.pk/cdn/shop/files/81Mya-dPIOL._AC_SL1500.webp?v=1731416529",
    description: "Smartphone dengan AI photography terbaik",
  },
];

// Helper Functions
function formatPrice(price) {
  return new Intl.NumberFormat("id-ID", {
    style: "currency",
    currency: "IDR",
    minimumFractionDigits: 0,
  }).format(price);
}

function getCartFromStorage() {
  const cart = localStorage.getItem("cart");
  return cart ? JSON.parse(cart) : [];
}

function saveCartToStorage(cart) {
  localStorage.setItem("cart", JSON.stringify(cart));
}

function addToCart(productId, quantity = 1) {
  const cart = getCartFromStorage();
  const product = PRODUCTS.find((p) => p.id === productId);

  if (!product) return false;

  const existingItem = cart.find((item) => item.id === productId);

  if (existingItem) {
    existingItem.quantity += quantity;
  } else {
    cart.push({
      id: productId,
      quantity: quantity,
    });
  }

  saveCartToStorage(cart);
  updateCartCount();
  return true;
}

function removeFromCart(productId) {
  let cart = getCartFromStorage();
  cart = cart.filter((item) => item.id !== productId);
  saveCartToStorage(cart);
  updateCartCount();
}

function updateCartQuantity(productId, quantity) {
  const cart = getCartFromStorage();
  const item = cart.find((c) => c.id === productId);

  if (item) {
    if (quantity <= 0) {
      removeFromCart(productId);
    } else {
      item.quantity = quantity;
      saveCartToStorage(cart);
    }
  }
  updateCartCount();
}

function updateCartCount() {
  const cart = getCartFromStorage();
  const count = cart.reduce((sum, item) => sum + item.quantity, 0);
  const cartCountEl = document.getElementById("cartCount");
  if (cartCountEl) {
    cartCountEl.textContent = count;
  }
}

function getProduct(productId) {
  return PRODUCTS.find((p) => p.id === productId);
}
