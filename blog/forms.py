from django import forms 
from .moedls import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class':'form-control'
        })
        self.fields['status'].widget.attrs.update({
            'class':'form-control'
        })