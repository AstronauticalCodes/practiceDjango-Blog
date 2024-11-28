from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Article

# Create your views here.
def index(request):
    num_articles = Article.objects.all().count()
    articles = Article.objects.all()
    context = {
        'greetings_to': 'Anonymous',
        'num_articles': num_articles,
        'articles': articles,
        'an': "helloworld"
    }
    return render(request, 'blogsite/index.html', context=context)


def list_of_articles(request):
    return HttpResponse("List of articles")


def contributors(request, name, age, experience):
    return HttpResponse(f"""
    <h2>Contributors of the community</h2>
    <p>Name: {name}</p>
    <p>Age: {age}</p>
    <p>Experience and some info you'd like to share: {experience}</p>
    """)


class ArticleDetailView(generic.DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'blogsite/article_list.html'

    def get_queryset(self):
        return Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_articles'] = Article.objects.all().count()
        context['greetings_to'] = 'Anonymous'
        return context

    def get_absolute_url(self):
        return reverse('article-details', args=[str(self.id)])
