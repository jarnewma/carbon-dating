from django.urls import path
from post import views


urlpatterns = [
    path("post/<int:id>/", views.post_detail, name="post_detail"),
    path("new_post/", views.new_post, name="new_post"),
]
