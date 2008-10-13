from django.db import models
from unicodedata import normalize
from re import sub

def slugify(title):
    name = normalize('NFKD', title).encode('ascii', 'ignore').replace(' ', '-').lower()
    #remove `other` characters
    name = sub('[^a-zA-Z0-9_-]', '', name)
    #nomalize dashes
    name = sub('-+', '-', name)

    return name

class Tag(models.Model):
    title = models.CharField(max_length=32)
    name = models.CharField(max_length=32, help_text="Leave empty for auto generation.", blank=True)

    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False):
        if not self.name:
            self.name = slugify(self.title)
        super(Post, self).save(force_insert, force_update)

    class Meta:
        ordering = ["name"]

class Post(models.Model):
    title = models.CharField(max_length=256)
    name = models.CharField(max_length=256, help_text="Leave empty for auto generation.", blank=True)
    content = models.TextField(max_length=8192)
    date = models.DateTimeField()
    disable_comments = models.BooleanField()
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False):
        if not self.name:
            self.name = slugify(self.title)
        super(Post, self).save(force_insert, force_update)

    class Meta:
        ordering = ["-date"]

class Page(models.Model):
    title = models.CharField(max_length=256)
    name = models.CharField(max_length=256, help_text="Leave empty for auto generation.", blank=True)
    content = models.TextField(max_length=8192)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False):
        if not self.name:
            self.name = slugify(self.title)
        super(Post, self).save(force_insert, force_update)

    class Meta:
        ordering = ["name"]


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

    class Meta:
        ordering = ["date"]

class Option(models.Model):
    name = models.CharField(max_length=32)
    value = models.TextField(max_length=2048)

    class Meta:
        ordering = ["name"]
