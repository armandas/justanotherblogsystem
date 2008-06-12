# -*- coding: UTF-8 -*-

from django import newforms as forms
from django.utils.translation import ugettext as _

class CommentForm(forms.Form):
    author_name = forms.CharField(label=_('Name'))
    author_email = forms.EmailField(label=_('E-mail'))
    author_website = forms.URLField(required=False, label=_('Website'))
    comment = forms.CharField(widget=forms.Textarea, label=_('Comment')
