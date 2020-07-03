from django.urls import path
from . import views
from .views import (PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
    latest_post)


#in blog folder
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #path('latest_post/<int:pk>', latest_post, name='latest_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]

