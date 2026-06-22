from django.contrib import admin
from .models import Category, Product, HeroBanner, CartItem, Order

# Kategoriyalar va mahsulotlar uchun
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

# Bannerlar uchun
@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)

# Savat uchun (ixtiyoriy, admin panelda ko'rinishi uchun)
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')

# Buyurtmalar uchun (Eng muhim qism)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Admin panelda ko'rinadigan ustunlar
    list_display = ('id', 'user', 'full_name', 'phone', 'status', 'created_at')
    
    # Ro'yxatdan turib o'zgartirish mumkin bo'lgan ustunlar
    list_editable = ('status',)
    
    # Filtrlash imkoniyati
    list_filter = ('status', 'created_at')
    
    # Qidiruv maydoni
    search_fields = ('full_name', 'phone')
    
    # Buyurtma yaratilgan sanani tartiblash
    ordering = ('-created_at',)