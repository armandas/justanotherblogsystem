from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response

from blogapp.models import *

def not_found(request, title='Error 404', message='Page not found'):
    t = get_template("service/404_message.html")
    c = Context({'title': title, 'message': message})
    html = t.render(c)
    return HttpResponseNotFound(html)