from django.shortcuts import render, get_object_or_404
from apps.onlineshop.models import Category, Product

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(avaliable = True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'onlineshop/product/list.html',{'category':category, 'categories':categories, 'products':products})

def product_detail(request, id, slug):
    product = get_object_or_404(product, id=id, slug=slug, avaliable=True)
    return render(request,'onlineshop/product/detail.html',{'product':product})
