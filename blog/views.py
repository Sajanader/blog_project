from django.shortcuts import render
from django.views.generic import TemplateView, DetailView , ListView
from .models import Post 
# Create your views here.
class HomeView(ListView):
    template_name = 'home.html'
    model = Post 
      
class PostDetailView(DetailView):
    template_name = 'post_details.html'  
    model = Post    