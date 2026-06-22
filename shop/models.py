from django.db import models
from django.contrib.auth.models import User

# 1. Kategoriya
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

# 2. Mahsulot
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    name = models.CharField(max_length=200, verbose_name="Mahsulot nomi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    image = models.ImageField(upload_to='products/', verbose_name="Rasm")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

# 3. Banner
class HeroBanner(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    image = models.ImageField(upload_to='banners/', verbose_name="Banner rasmi")
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlar"

# 4. Savat elementi
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Savat elementi"
        verbose_name_plural = "Savat elementlari"

# 5. Buyurtma
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100, verbose_name="Ism-sharif")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqam")
    address = models.TextField(verbose_name="Manzil")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vaqti")
    status = models.CharField(max_length=20, default="Yangi", verbose_name="Holati")



    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"