from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('notes/', views.notes_list),
    path('notes/<int:pk>/', views.notes_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)