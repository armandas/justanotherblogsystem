# -*- coding: utf-8 -*-

from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from md5 import md5
from urllib import quote

from blogapp.utilities.friends import rel_decode
from blogapp.utilities import options

register = template.Library()

def dgs(number, word=''):
    """Pluralization for Lithuanian (works partially)

       Kaip argumentą pateikite daugiskaitos vardininką
        - Pvz1: {{ 10|dgs:"Komentarai"}}
        - Pvz2: {{ 21|dgs:"Knygos"}}
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

def gravatar(email):
    gravatar_id = md5(email).hexdigest()
    gravatar_size = options('gravatar_size')
    default_uri = quote(options('default_gravatar_uri'), safe='')
    uri = "http://www.gravatar.com/avatar.php?gravatar_id=%s&size=%s&default=%s"
    return uri % (gravatar_id, gravatar_size, default_uri)

#register filters
register.filter(dgs)
register.filter(nl2br)
register.filter(link_tags)
register.filter(rel_decode) #imported
register.filter(gravatar)