from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=250, help_text='Enter a title for a new article')
    text = models.CharField(max_length=1000, help_text='Place your story here')
    author = models.ForeignKey('Contributor', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    name = models.CharField(max_length=250, help_text='Enter first name of the contributor')
    surname = models.CharField(max_length=500, help_text='Enter surname of the contributor')
    about = models.CharField(max_length=2000, help_text='Tell us about yourself, your experience and current work')
    email = models.EmailField(null=True, blank=True)

    class Meta:
        ordering = ['surname', 'name']

    def __str__(self):
        return f'{self.surname}, {self.name}'


# Contributor.objects.create(name="Robert", surname="Wright", about="Very demure", email="anything@gmail.com")
#
# Article.objects.bulk_create(
#     [
#     Article(title="Tutorial about blog making", text="Today we're going to create blog", author=Contributor.objects.filter(name='Robert').first(), date=date.today()),
#     Article(title='New article about Django', text="Let's talk about view functions and classe", author=Contributor.objects.filter(name='Robert').first(), date=date.today())
#     ]
# )c
