from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
# ================= CUSTOM USER MODEL =================
class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=10, default='customer')

    class Meta:
        db_table = 'users'


# ================= PRODUCT MODEL =================
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    trending = models.BooleanField(default=False)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.product_name


# ================= DISCOUNT MODEL =================
class Discount(models.Model):
    discount_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    end_time = models.DateTimeField()

    class Meta:
        db_table = 'discounts'

    def __str__(self):
        return f"{self.product.product_name} - {self.discounted_price}"


# ================= CART MODEL =================
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cart'


# ================= ORDER MODEL =================
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('processing', 'Processing'),
            ('shipped', 'Shipped'),
            ('delivered', 'Delivered'),
            ('cancelled', 'Cancelled')
        ],
        default='pending'
    )
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'


# ================= ORDER ITEM MODEL =================
class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_items'
# models.py (add at the bottom)
class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banner_images/Mega Deal')
    link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'banners'

    def __str__(self):
        return self.title

# Add flash_deal to Product
Product.add_to_class('flash_deal', models.BooleanField(default=False))
