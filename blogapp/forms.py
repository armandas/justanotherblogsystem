# -*- coding: UTF-8 -*-

from django import newforms as forms

class CommentForm(forms.Form):
    author_name = forms.CharField(label='Vardas')
    author_email = forms.EmailField(label='E-paštas')
    author_website = forms.URLField(required=False, label='Svetainė')
    comment = forms.CharField(widget=forms.Textarea, label='Komentaras')
