from django.urls import path
from . import views

app_name = 'Calendar'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.detail, name='detail'),
    path('test/', views.cal, name='cal'),
]