from django.views.generic import ListView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
