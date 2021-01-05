from django.shortcuts import render
from django.views.generic import TemplateView, DetailView , ListView , CreateView , UpdateView, DeleteView
from .models import Post 
from django.urls import reverse_lazy
# Create your views here.
class HomeView(ListView):
    template_name = 'home.html'
    model = Post 
      
class PostDetailView(DetailView):
    template_name = 'post_details.html'  
    model = Post    

class PostCreateView(CreateView):
    template_name = 'blog_create.html'  
    model = Post 
    fields = ['title', 'auther' , 'body']

class PostUpdateView(UpdateView):
    template_name = 'blog_update.html'  
    model = Post 
    fields = ['title', 'auther' , 'body']    
  
class PostDeleteView(DeleteView):
    template_name = 'blog_delete.html'  
    model = Post 
    fields = ['title', 'auther' , 'body'] 
    success_url = reverse_lazy('home')     


     