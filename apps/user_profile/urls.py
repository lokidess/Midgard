from django.urls import path

from apps.user_profile import views

app_name = 'user_profile'

urlpatterns = [
    path('user/profile/view/<int:user_id>', views.UserProfileView.as_view(), name='view_profile'),
    path('user/create/', views.UserRegistrationView.as_view(), name='create_user'),
    path('user/login/', views.UserAuthorizationView.as_view(), name='login'),
    path('user/logout/', views.UserLogoutView.as_view(), name='logout'),
    path('user/<str:slug>', views.UserSelfProfileView.as_view(), name='view_self_profile'),
]
