from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
from .models import Product, Cart, Order, OrderItem, Discount, Banner

# -------------------- HOME PAGE --------------------
def index(request):
    # Use 'is_active' instead of 'active'
    banners = Banner.objects.filter(is_active=True)
    categories = Product.objects.values_list('category', flat=True).distinct()
    context = {
        'banners': banners,
        'categories': categories,
        'site_name': 'ZoVo',
    }
    return render(request, 'index.html', context)
   
# -------------------- CATEGORY VIEW --------------------
def category_view(request, category_name):
    products = Product.objects.filter(category=category_name)
    categories = Product.objects.values_list("category", flat=True).distinct()
    return render(request, "category.html", {
        "products": products,
        "category": category_name,
        "categories": categories
    })

# -------------------- CART --------------------
@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, "cart.html", {
        "cart_items": cart_items,
        "total": total
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("cart_view")

@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, pk=cart_id, user=request.user)
    cart_item.delete()
    return redirect("cart_view")

@login_required
def update_cart_item(request, cart_id):
    if request.method == "POST":
        cart_item = get_object_or_404(Cart, pk=cart_id, user=request.user)
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect("cart_view")

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, "checkout.html", {
        "cart_items": cart_items,
        "total": total
    })

@login_required
def orders_view(request):
    user_orders = Order.objects.filter(user=request.user)
    return render(request, "orders.html", {"orders": user_orders})

# -------------------- AJAX PRODUCTS --------------------
def ajax_products(request):
    """
    Returns all products, trending products, flash deals, and hero banners as JSON.
    """
    now = timezone.now()

    # Fetch all products as model instances
    all_products = Product.objects.all()
    trending_products = Product.objects.filter(trending=True)

    # Flash deals: products with active discount
    flash_discounts = Discount.objects.filter(end_time__gt=now).select_related('product')
    flash_deals = []
    for d in flash_discounts:
        p = d.product
        flash_deals.append({
            "product_id": p.product_id,
            "name": p.product_name,
            "description": p.description,
            "category": p.category,
            "price": float(p.price),
            "stock_quantity": p.stock_quantity,
            "image_url": p.image.url if p.image else None,
            "discounted_price": float(d.discounted_price),
            "discount_end_time": d.end_time.isoformat()
        })

    # Hero banners
    hero_offers = Banner.objects.filter(is_active=True)
    hero_data = []
    for b in hero_offers:
        hero_data.append({
            "title": b.title,
            "link": b.link,
            "image_url": b.image.url if b.image else None
        })

    # Convert products to JSON-friendly dict
    def serialize_product(p):
        return {
            "product_id": p.product_id,
            "name": p.product_name,
            "description": p.description,
            "category": p.category,
            "price": float(p.price),
            "stock_quantity": p.stock_quantity,
            "image_url": p.image.url if p.image else None
        }

    return JsonResponse({
        "all_products": [serialize_product(p) for p in all_products],
        "trending_products": [serialize_product(p) for p in trending_products],
        "flash_deals": flash_deals,
        "hero_offers": hero_data
    })
