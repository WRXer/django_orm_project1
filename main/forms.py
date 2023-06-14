from django import forms
from main.models import Blogs, Product


class AppBlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        exclude = ['id']
        fields = ['name', 'slug', 'description', 'is_published', 'image']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('created_at', 'recreated_at')

    def clean_name(self):
        name = self.cleaned_data['name']
        # Проверка наличия запрещенных слов
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in name.lower():
                raise forms.ValidationError("Недопустимое слово в названии продукта.")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        # Проверка наличия запрещенных слов
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in description.lower():
                raise forms.ValidationError("Недопустимое слово в описании продукта.")
        return description

