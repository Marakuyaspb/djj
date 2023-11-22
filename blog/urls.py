from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.blog, name = 'blog'),
    path('tag/<slug:tag_slug>/',
        views.blog, name='blog_by_tag'),

    # posts dynamic
    path('blog/<int:id>/', views.single_blog_post, name='single_blog_post'),
]