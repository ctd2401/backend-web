from msilib.schema import ListView
from multiprocessing import context
import re
from django.urls import reverse
from tempfile import template
from urllib import request
from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import (CreateView,
                                    DeleteView,
                                    DetailView,
                                    ListView,
                                    UpdateView)
# Create your views here.
class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()
class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    queryset = Article.objects.all()
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)
class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)    
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    queryset = Article.objects.all()
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)
    def get_success_url(self):
        return reverse('blog:article-list')
