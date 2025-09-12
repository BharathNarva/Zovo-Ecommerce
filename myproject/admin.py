from django.contrib import admin
from .models import User, Product, Discount, Cart, Order, OrderItem, Banner

# ====================== USER ADMIN ======================
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone')


# ====================== PRODUCT ADMIN ======================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'stock_quantity', 'trending', 'flash_deal', 'date_added')
    list_filter = ('trending', 'flash_deal', 'category')
    search_fields = ('product_name', 'category', 'description')
    readonly_fields = ('date_added',)
    # Optional: Add a checkbox to quickly toggle trending or flash deal
    list_editable = ('trending', 'flash_deal')


# ====================== DISCOUNT ADMIN ======================
@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('product', 'discounted_price', 'end_time')
    list_filter = ('end_time',)
    search_fields = ('product__product_name',)


# ====================== CART ADMIN ======================
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'date_added')
    search_fields = ('user__username', 'product__product_name')


# ====================== ORDER ADMIN ======================
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'total_amount', 'order_status', 'order_date')
    list_filter = ('order_status', 'order_date')
    search_fields = ('user__username',)


# ====================== ORDER ITEM ADMIN ======================
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__order_id', 'product__product_name')


# ====================== BANNER ADMIN ======================
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title',)
    readonly_fields = ('created_at',)
