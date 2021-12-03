from django.shortcuts import render
from mainapp.models import ProductCategory, Product
from django.shortcuts import get_object_or_404


def index(request):
    context = {
        'title': 'Главная',
        'products': Product.objects.all()[:4],
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    title = 'Продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }
        return render(request, 'mainapp/products_list.html', context)

    same_products = Product.objects.all()[3:5]
    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contact.html', context)
