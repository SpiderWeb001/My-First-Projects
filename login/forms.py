from loginpage.models import Post
from django import forms


class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ('title', 'text')
