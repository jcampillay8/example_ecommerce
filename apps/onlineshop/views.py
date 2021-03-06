from django.shortcuts import render, get_object_or_404
from apps.onlineshop.models import Category, Product
from apps.cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(avaliable = True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'onlineshop/product/list.html',{'category':category, 'categories':categories, 'products':products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, avaliable=True)
    cart_product_form=CartAddProductForm()
    return render(request,'onlineshop/product/detail.html',{'product':product,'cart_product_form':cart_product_form})
