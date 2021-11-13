from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Post
from .forms import AppendPost
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request,'index.html') 

class articles(ListView):
    model=Post
    template_name="articles.html"

class showdetails(DetailView):
    model=Post
    template_name="details.html"
  
class addpost(CreateView):
    model=Post
    form_class=AppendPost
    template_name='addpost.html'

class editview(UpdateView):
    model=Post
    form_class=AppendPost
    template_name='editpost.html'

class deleteview(DeleteView):
    model=Post
    success_url=reverse_lazy('articles')
    template_name='deletepost.html'
    