from django.urls import path
from . import views

urlpatterns = [
    # Bosh sahifa
    path('', views.index, name='index'),
    
    # Mahsulot detal sahifasi (ID bo'yicha)
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    
    # Savat sahifasi
    path('cart/', views.cart_view, name='cart'),
    
    # Savatga mahsulot qo'shish
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
    # Buyurtma berish sahifasi
    path('checkout/', views.checkout, name='checkout'),
    
    # Foydalanuvchi profili
    path('profile/', views.profile, name='profile'),

    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),


]