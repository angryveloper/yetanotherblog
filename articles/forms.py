from django import forms

from .models import Article, Comment


class NewArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
