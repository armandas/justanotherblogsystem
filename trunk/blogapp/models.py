from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=32)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Admin:
        list_per_page = 15

class Post(models.Model):
    title = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    content = models.TextField(max_length=8192)
    date = models.DateTimeField()
    disable_comments = models.BooleanField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Admin:
        list_display = ('title', 'content', 'date',)
        list_filter = ('disable_comments', 'tags',)
        ordering = ('-date',)
        search_fields = ('title', 'content')
        list_per_page = 15

    class Meta:
        ordering = ["-date"]


class Comment(models.Model):

    TYPE_CHOICES = (
        ('comment', 'comment'),
        ('unread', 'unread'),
        ('spam', 'spam'),
        ('linkback', 'linkback'),
    )

    author_name = models.CharField(max_length=48)
    author_email = models.EmailField(blank=True)
    author_website = models.URLField(blank=True)
    author_ip = models.IPAddressField(blank=True, null=True)
    date = models.DateTimeField()
    post = models.ForeignKey(Post)
    content = models.TextField(max_length=2048)
    comment_type = models.TextField(max_length=10, choices=TYPE_CHOICES)

    class Admin:
        list_display = ('author_name', 'content', 'post', 'date', 'comment_type')
        list_filter = ('comment_type', 'post')
        ordering = ('-date',)
        search_fields = ('author_name', 'author_email', 'author_website', 'author_ip' 'content')
        list_per_page = 15

    class Meta:
        ordering = ["date"]

class Option(models.Model):
    name = models.CharField(max_length=32)
    value = models.TextField(max_length=2048)

    class Admin:
        list_display = ('name', 'value')
        ordering = ('name',)
        search_fields = ('name', 'value')
        list_per_page = 15
