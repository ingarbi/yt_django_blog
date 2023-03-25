from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from blog.forms import PostSearchForm
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
    related = Post.objects.filter(author=post.author)[:5]
    return render(
        request,
        "blog/components/single-post-elements.html",
        {"post": post, "related": related},
    )


class TagListView(HomeView):

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/tags-list-elements.html"
        return "blog/tags.html"

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs["tag"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.kwargs["tag"]
        return context
    
class PostSearchView(HomeView):
    form_class =PostSearchForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Post.objects.filter(title__icontains=form.cleaned_data["q"])

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/search-list-elements.html"
        return "blog/search.html"