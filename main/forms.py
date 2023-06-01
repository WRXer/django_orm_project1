from django import forms
from main.models import Blogs


class AppBlogsForm(forms.ModelForm):

    class Meta:
        model = Blogs
        exclude = ['id']
        fields = ['name', 'slug', 'description', 'is_published', 'image']
