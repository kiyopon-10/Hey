from django.urls import path
from .views import main_view
from . import views

urlpatterns = [
    path('', main_view, name='main_view'),
    path('api/check-room-existence/', views.check_room_existence, name='check-room-existence'),
]