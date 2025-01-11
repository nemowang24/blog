from django.urls import path
from .views import post_list,AboutPageView, post_detail,post_list2

urlpatterns = [
    path("", post_list, name="home"),
    path("test", post_list2, name="home2"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
]