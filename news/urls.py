from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page>/', views.archives, name='archives'),
    path('post_<int:entry>/', views.view_post, name='viewpost'),
]