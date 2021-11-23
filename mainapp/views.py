import json
import os.path

from django.shortcuts import render


def main(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)


module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'fixtures/links_menu.json')
links_menu = json.load(open(file_path, encoding='utf-8'))


def products(request):
    context = {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)


def products_home(request):
    context = {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)


def products_office(request):
    context = {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)


def products_modern(request):
    context = {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)


def products_classic(request):
    context = {
        'title': 'Продукты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contact.html', context)

# Create your views here.
