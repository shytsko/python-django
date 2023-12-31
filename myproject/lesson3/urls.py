from django.urls import path
from .views import hello, HelloView, posts, PostsView, posts_detail, TemplIf, TemplFor, author_posts, post_full

urlpatterns = [
    path('hello/<str:name>/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', posts, name='year_post'),
    path('posts/<int:year>/<int:month>/', PostsView.as_view(), name='year_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', posts_detail, name='posts_detail'),
    path('if/<int:number>', TemplIf.as_view(), name='if'),
    path('for/', TemplFor.as_view(), name='for'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full'),
]
