from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_event, name='create_event'),
    path('register/<int:event_id>/', views.register_event, name='register_event'),
]
