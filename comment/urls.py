from django.urls import path
from comment import views


urlpatterns = [
    path("post/<int:id>/add_comment/", views.new_comment, name="add_comment"),
]
