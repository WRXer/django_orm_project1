from django.shortcuts import render

from main.models import Category


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