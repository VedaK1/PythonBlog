from django import forms
from .models import Post

class AppendPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title",'author','desc','code']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
            'code':forms.Textarea(attrs={'class':'form-control'})
        }