from django.forms import formset_factory, inlineformset_factory
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy
from main.models import Category, Product, Blogs, Contacts, Version
from .forms import AppBlogsForm, ProductForm, VersionForm


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


class ProductsCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:products')


class ProductsUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductsListView(generic.ListView):
    model = Product
    extra_context = {
        'title': 'Все товары'
    }
    context_object_name = 'products'
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['products']
        for product in products:
            product.active_version = product.get_active_version()
        return context


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


class BlogsUpdateView(generic.UpdateView):
    model = Blogs
    form_class = AppBlogsForm
    template_name = 'main/update_blogs.html'
    #success_url = 'main/blog_detail/<int:pk>/'  # Перенаправление после успешного создания статьи

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.object.get_absolute_url())


class BlogsDeleteView(generic.DeleteView):
    model = Blogs    #Модель
    success_url = reverse_lazy('main:blogs')    #Адрес для перенаправления после успешного удаления

