from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_ideas),
    path('create-idea/', views.create_idea),
    path('delete-idea/<int:idea_id>/', views.delete_idea),
    path("<int:idea_id>/", views.view_idea),
    path("likes/<int:idea_id>/", views.create_like),
]