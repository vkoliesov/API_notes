from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('notes', views.NoteViewSet, basename='notes')

urlpatterns = router.urls


# notes_list = views.NoteViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
#     })

# notes_detail = views.NoteViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
#     })

# urlpatterns = [
#     path('notes/', notes_list, name='notes-list'),
#     path('notes/<int:pk>/', notes_detail, name='notes-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)