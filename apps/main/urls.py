from django.urls import path

from apps.main import views

app_name = 'main'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page')
]
