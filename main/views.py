from django.shortcuts import render, get_object_or_404

from main.models import Category, Product


# Create your views here.
def index(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Главная'
    }
    return render(request, 'main/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contact.html', context)


def products(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Все товары'
    }
    for product in products_list:
        if len(product.description) > 100:
            product.description = product.description[:100] + "..."
    return render(request, 'main/products.html', context)


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'main/product_details.html', {'product': product})
