from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('create_account/', views.create_account, name='createaccount'),
    path('user_<str:username>/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('climatescience/<int:page>/', views.climate_science, name='climatescience'),
    path('climatescience/post_<int:entry>/', views.climate_science_entry, name='climatescienceentry'),
    path('environmentalscience/<int:page>/', views.environmental_science, name='environmentalscience'),
    path('environmentalscience/post_<int:entry>/', views.environmental_science_entry, name='environmentalscienceentry'),
    path('ecology/<int:page>/', views.ecology, name='ecology'),
    path('ecology/post_<int:entry>/', views.ecology_entry, name='ecologyentry'),
    path('technology/<int:page>/', views.technology, name='technology'),
    path('technology/post_<int:entry>/', views.technology_entry, name='technologyentry'),
    path('<str:subject>/addtopic/', views.add_topic, name='addtopic'),
]

urlpatterns += staticfiles_urlpatterns()
