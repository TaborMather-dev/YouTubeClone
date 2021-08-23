from django.urls import path
from . import views

urlpatterns = [
    path("youtubeclone_app/", views.CommentList.as_view()),
    path("youtubeclone_app-id/<str:video_id>/", views.CommentDetail.as_view()),
    path("youtubeclone_app-like/<int:id>/", views.CommentLike.as_view()),
    path("youtubeclone_app-dislike/<int:id>/", views.CommentDislike.as_view()),
    path("youtubeclone_app-reply/", views.ReplyList.as_view()),
    path("youtubeclone_app-reply/<int:comment>/", views.ReplyDetail.as_view()),
]
