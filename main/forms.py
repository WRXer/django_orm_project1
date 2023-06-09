from django import forms
from main.models import Blogs, Product, Version


class AppBlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        #exclude = ['id']

        fields = ['name', 'slug', 'description', 'is_published', 'image']



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price', 'is_active')
        #exclude = ('created_at', 'recreated_at', 'product_owner', 'is_active')


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



class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('version_number', 'version_name', 'is_active')