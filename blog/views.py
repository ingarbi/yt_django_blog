from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Post


class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status="published")
    return render(request, "blog/components/single-post-elements.html", {"post": post})
