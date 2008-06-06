# -*- coding: utf-8 -*-

from django import template
from django.core.urlresolvers import reverse

register = template.Library()

def dgs(number, word=''):
    """Pluralization for Lithuanian

       Kaip argumentą pateikite daugiskaitos vardininką
        - Pvz1: {{ 10|plural:"Komentarai"}}
        - Pvz2: {{ 21|plural:"Knygos"}}
    """
    if number in range(11,20) or (number % 10) == 0:
        #masculine and feminine forms are the same
        word = word[:-2] + u"ų"

    elif number == 1 or (number % 10) == 1:
        if word[-2:] == "ai":
            #masculine form
            word = word[:-2] + "as"
        elif word[-2:] == "os":
            #feminine form
            word = word[:-2] + "a"

    #default value is used in all other cases
    return "%d %s" % (number, word)

def nl2br(value):
    """Converts newlines into <br>s rather than <br />s"""
    return value.replace('\n', '                    <br>')

def link_tags(taglist):
    return ['<a href="%s">%s</a>' % (reverse('blogapp.views.posts_by_tag', args=[tag.name]), tag.title) for tag in taglist]


#register filters
register.filter(dgs)
register.filter(nl2br)
register.filter(link_tags)