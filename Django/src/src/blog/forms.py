from cProfile import label
from logging import PlaceHolder
from turtle import title
from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'author',
            'date',
        ]
    title       =forms.CharField(label='',
                    widget=forms.TextInput(attrs={"placeholder":"Article title"})
                )
    content     = forms.CharField(
                    required=True, 
                    widget=forms.Textarea(
                        attrs={
                            "placeholder": "Article content",
                            "class": "new-class-name-two",
                            "id": "my-id-for-textarea",
                            "rows":10,
                            "cols":50,
                        }
                    )
    )
    author      = forms.CharField()
    date        = forms.DateTimeField()
