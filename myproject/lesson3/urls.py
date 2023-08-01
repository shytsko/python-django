from django.urls import path
from .views import hello, HelloView, posts, PostsView, posts_detail

urlpatterns = [
    path('hello/<str:name>/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', posts, name='year_post'),
    path('posts/<int:year>/<int:month>/', PostsView.as_view(), name='year_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', posts_detail, name='posts_detail'),
]
