# myproject/urls.py

from django.contrib import admin
from django.urls import path
from myproject import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page
    path('', views.index, name='index'),

    # Cart pages
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),

    # Checkout
    path('checkout/', views.checkout, name='checkout'),

    # Orders page
    path('orders/', views.orders_view, name='orders_view'),

    # Category page
    path('category/<str:category_name>/', views.category_view, name='category_view'),

    # AJAX endpoint for live products
    path('ajax/products/', views.ajax_products, name='ajax_products'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
