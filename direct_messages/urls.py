from django.urls import path
from direct_messages import views


url_patterns = [
    path('messages/<str:username>/',
         views.MessagesView.as_view(), name="direct_messages"),
    path('messages/', views.AllMessages.as_view(), name="all_messages")

]
