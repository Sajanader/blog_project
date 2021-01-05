from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.

class PostCRUDTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'sdra' , 
            email = 'sdra@sdra.com' , 
            password = '0123456789'
        )
        self.post = Post.objects.create(
            title = 'physics' , 
            auther = self.user , 
            body = 'physics is an interesting science'
        )
    def test_home_page(self): 
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code , 200) 

    def test_details_page(self): 
        response = self.client.get(reverse('post_details' , args = '1'))
        self.assertEqual(response.status_code , 200) 

    def test_details_page_elements(self): 
        response = self.client.get(reverse('post_details' , args = '1'))
        self.assertContains(response , 'physics')  

    def test_blog_update(self): 
        response = self.client.post(reverse('blog_update' , args = '1'),{
            'body': 'physics is a hard science',
        })
        self.assertContains(response, 'physics is a hard science')              



