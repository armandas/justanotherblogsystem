from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from blogapp.models import *

def homepage(request):
    posts = Post.objects.all()[:5]
    template = get_template('blog.html')
    html = template.render(Context({'posts': posts,}))
    return HttpResponse(html)

def post_by_name(request, post_name, dummy_comments=''):
    try:
        post = Post.objects.get(name=post_name)
        comments = post.comment_set.all()
        template = get_template('blog.html')

        context = Context({
            'posts': [post],
            'comments': comments,
            'title': post.title + " // ",
            })
        html = template.render(context)
    except:
        template = get_template('404.html')
        html = template.render(Context({'title': ['Error 404']}))
    return HttpResponse(html)

def posts_by_tag(request, tag_name):
    try:
        tag = Tag.objects.get(name=tag_name)
        posts = tag.post_set.all()[:5]
        template = get_template('blog.html')
        html = template.render(Context({'posts': posts,}))
    except:
        template = get_template('404.html')
        html = template.render(Context({'title': ['Error 404']}))
    return HttpResponse(html)

def posts_by_date(request, year, month):
    posts = Post.objects.filter(date__year=year, date__month=month)[:5]
    template = get_template('blog.html')
    html = template.render(Context({'posts': posts,}))
    return HttpResponse(html)

def foto(request):
    post = {}
    post['name'] = 'Test'
    post['content'] = '<p>This is a test post :P</p>'
    post['date'] = datetime.datetime(2008, 5, 2, 23, 24)
    post['comment_count'] = 3
    photo = True
    #comments = post.comment_set.all()

    t = get_template('foto.html')
    html = t.render(Context({'post': post, 'comments': comments, 'photo': photo}))
    return HttpResponse(html)
