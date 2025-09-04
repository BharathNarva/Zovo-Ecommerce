# myproject/urls.py

from django.contrib import admin
from django.urls import path
from myproject.views import (
    index,
    cart_view,
    add_to_cart,
    remove_from_cart,
    checkout,
    orders_view
)

# ✅ Add these imports
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page
    path('', index, name='index'),

    # Cart pages
    path('cart/', cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),

    # Checkout
    path('checkout/', checkout, name='checkout'),

    # Orders page
    path('orders/', orders_view, name='orders_view'),
]

# ✅ Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
