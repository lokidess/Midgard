from django.urls import path
from django.contrib.auth import views as auth_views

from apps.user_profile import views

app_name = 'user_profile'

urlpatterns = [
    path('profile/view/<int:user_id>', views.UserProfileView.as_view(), name='view_profile')
]
