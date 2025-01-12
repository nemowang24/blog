from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"

class BlogDetailView(DetailView):
    model =Post
    template_name = "post_detail.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "51 Jordan Lane"
        context["phone_number"] = "845-978-8174"
        return context

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    model=Post
    template_name = "post_edit.html"
    fields=["title","body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
