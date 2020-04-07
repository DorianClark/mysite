from django.urls import path

from . import views

app_name='news'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:story_id>/', views.detail, name='detail'),
]