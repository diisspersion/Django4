from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),

]