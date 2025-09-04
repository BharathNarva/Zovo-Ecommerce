# myproject/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, Order, OrderItem, User

# ================= HOME PAGE =================
def index(request):
    """
    Display all products on the home page
    """
    products = Product.objects.all()  # Get all products
    return render(request, 'index.html', {'products': products})

# ================= CART VIEW =================
@login_required
def cart_view(request):
    """
    Show current logged-in user's cart items
    """
    cart_items = Cart.objects.filter(user=request.user)  # Only this user's items
    total = sum(item.product.price * item.quantity for item in cart_items)  # Total cost
    return render(request, "cart.html", {"cart_items": cart_items, "total": total})

# ================= ADD TO CART =================
@login_required
def add_to_cart(request, product_id):
    """
    Add a product to the cart or increase its quantity if it already exists
    """
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1  # Increment quantity if already in cart
        cart_item.save()

    return redirect("cart_view")  # Redirect to cart page

# ================= REMOVE FROM CART =================
@login_required
def remove_from_cart(request, cart_id):
    """
    Remove a cart item for the logged-in user
    """
    cart_item = get_object_or_404(Cart, pk=cart_id, user=request.user)
    cart_item.delete()
    return redirect("cart_view")
# ================= UPDATE CART ITEM QUANTITY =================
@login_required
def update_cart_item(request, cart_id):
    """
    Update the quantity of a cart item for the logged-in user
    """
    if request.method == "POST":
        cart_item = get_object_or_404(Cart, pk=cart_id, user=request.user)
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()  # Remove item if quantity is zero or less
    return redirect("cart_view")
# ================= CHECKOUT =================
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total})
from django.shortcuts import render
from .models import Order

@login_required
def orders_view(request):
    """Display all orders for the logged-in user"""
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': user_orders})
