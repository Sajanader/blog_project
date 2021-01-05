from django.urls import path , include
from .views import HomeView , PostDetailView , PostCreateView , PostUpdateView , PostDeleteView

urlpatterns = [
    path('', HomeView.as_view() , name = 'home'),
    path('<int:pk>/', PostDetailView.as_view(), name = 'post_details'),
    path('post/new/' , PostCreateView.as_view(), name = 'create'),
    path('post/<int:pk>/edit/' , PostUpdateView.as_view(), name = 'blog_update'),
    path('post/<int:pk>/delete/' , PostDeleteView.as_view(), name = 'blog_delete'),
]
