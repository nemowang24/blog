from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import TemplateView

# Create your views here.

def post_list(request):
    posts=Post.objects.all()
    return render(request,"home.html",{'posts':posts})

def post_list2(request):
    posts=Post.objects.all()
    return render(request,"home2.html",{'posts':posts})

def post_detail(request,pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html",{"post":post})

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "51 Jordan Lane"
        context["phone_number"] = "845-978-8174"
        return context