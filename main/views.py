from django.views import generic
from main.models import Category, Product, Blogs, Contacts
from .forms import AppBlogsForm


# Create your views here.
class IndexListView(generic.ListView):
    model = Category
    extra_context = {
        'title': 'Главная'
    }


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'main/contact.html', context)
class ContactCreateView(generic.CreateView):
    model = Contacts
    template_name = "main/contact.html"
    fields = ('name', 'email', 'message')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Наши контакты"
        return context_data


class ProductsListView(generic.ListView):
    model = Product
    extra_context = {
        'title': 'Все товары'
    }


class ProductsDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        #context_data['title'] = context_data['object']
        return context_data

class BlogsListView(generic.ListView):
    model = Blogs
    extra_context = {
        'title': 'Блог'
    }
    template_name = "main/blogs_list.html"

    def get_queryset(self):
        """
        Фильтруйте статьи по положительному признаку публикации
        """
        return Blogs.objects.filter(is_published=True)


class BlogsDetailView(generic.DetailView):
    model = Blogs
    template_name = 'main/blog_detail.html'
    context_object_name = 'blog'

    def get(self, request, *args, **kwargs):
        """
        Увеличиваем счетчик просмотров
        """
        self.object = self.get_object()
        self.object.blog_views += 1
        self.object.save()

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class BlogsCreateView(generic.CreateView):
    model = Blogs
    form_class = AppBlogsForm
    template_name = 'main/create_blogs.html'
    success_url = '/blogs/'  # Перенаправление после успешного создания статьи