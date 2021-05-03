from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.ApiListView.as_view())
]