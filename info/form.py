from django import forms

from info.models import InfoBlog


class InfoBlogForm(forms.ModelForm):
    class Meta:
        model = InfoBlog
        fields = ('name', 'text', 'rating', 'price')
