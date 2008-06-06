from django.db import models


class Tag(models.Model):
    title = models.CharField(maxlength=32)
    name = models.CharField(maxlength=32)

    def __str__(self):
        return self.name

    class Admin:
        pass

class Post(models.Model):
    title = models.CharField(maxlength=256)
    name = models.CharField(maxlength=256)
    content = models.TextField(maxlength=8192)
    date = models.DateTimeField()
    photo = models.BooleanField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Admin:
        list_display = ('title', 'content', 'date')
        list_filter = ('tags',)
        ordering = ('-date',)
        search_fields = ('title', 'content')

    class Meta:
        ordering = ["-date"]


class Meta(models.Model):
    created = models.DateField()
    camera = models.CharField(maxlength=32)
    exposure = models.CharField(maxlength=10)
    aperture = models.CharField(maxlength=4)
    focal_length = models.CharField(maxlength=8)
    flickr_url = models.CharField(maxlength=256)
    description = models.TextField(maxlength=256)
    photo = models.OneToOneField(Post)

    class Admin:
        pass

class Comment(models.Model):
    author_name = models.CharField(maxlength=32)
    author_email = models.EmailField()
    author_website = models.URLField()
    author_ip = models.IPAddressField()
    date = models.DateTimeField()
    post = models.ForeignKey(Post)
    content = models.TextField(maxlength=2048)

    class Admin:
        list_display = ('author_name', 'content', 'date')
        list_filter = ('post',)
        ordering = ('-date',)
        search_fields = ('author_name', 'author_email', 'author_website', 'author_ip' 'content')

    class Meta:
        ordering = ["date"]
