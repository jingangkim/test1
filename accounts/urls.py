from django.urls import path
from . import views
from .views import UserProfileView

urlpatterns = [
    path('api/user/profile/<str:username>/', UserProfileView.as_view(), name='user_profile'),
    ]