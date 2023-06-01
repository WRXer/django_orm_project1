from django import forms
from main.models import Blogs


class AppBlogsForm(forms.ModelForm):
    """name = forms.CharField(max_length=100)
    slug = forms.SlugField(null=False, unique=True)
    description = forms.CharField(max_length=100)
    is_published = forms.BooleanField()
    image = forms.ImageField(null=False)"""

    class Meta:
        model = Blogs
        exclude = ['id']
        fields = ['name', 'slug', 'description', 'is_published', 'image']
