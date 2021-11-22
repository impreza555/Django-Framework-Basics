from django.shortcuts import render


def main(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Продукты',
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contact.html', context)

# Create your views here.
