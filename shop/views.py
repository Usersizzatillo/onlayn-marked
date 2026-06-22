from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, CartItem, Order

# 1. Bosh sahifa: Qidiruv va Kategoriya filtri bilan
def index(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    
    products = Product.objects.all()
    
    if query:
        products = products.filter(name__icontains=query)
    if category_id:
        products = products.filter(category_id=category_id)
        
    categories = Category.objects.all()
    cart_count = CartItem.objects.count()
    
    return render(request, 'index.html', {
        'products': products, 
        'categories': categories,
        'query': query,
        'selected_category': category_id,
        'cart_count': cart_count
    })

# 2. Mahsulot detali
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# 3. Savatni ko'rish
def cart_view(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

# 4. Savatga qo'shish (Xatoliksiz versiya)
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # get_or_create o'rniga filter().first() dan foydalanamiz
    cart_item = CartItem.objects.filter(product=product).first()
    
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        CartItem.objects.create(product=product, quantity=1)
        
    return redirect('cart')

# 5. Buyurtma berish (Checkout)
def checkout(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        # Order yaratish
        Order.objects.create(full_name=full_name, phone=phone, address=address)
        
        # Buyurtma berilgach savatni tozalash
        cart_items.delete()
        
        return redirect('index') # Bosh sahifaga qaytarish
        
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})

# 6. Profil sahifasi
def profile(request):
    return render(request, 'profile.html')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')