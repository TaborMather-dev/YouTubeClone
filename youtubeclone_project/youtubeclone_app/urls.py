from django.urls import path
from . import views


urlpatterns = [
    path('youtubeclone_app/', views.CommentList.as_view()),
]
