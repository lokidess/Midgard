from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import TemplateView, CreateView

from apps.user_profile.forms import RegistrationForm
from apps.user_profile.models import UserModel


class UserProfileView(TemplateView):
    """
    This view for look user profile
    """
    template_name = 'user_profile/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['full_name'] = get_user_model().objects.get(id=kwargs['user_id']).get_full_name()
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.id == kwargs['user_id']:
            slug = request.user.slug if request.user.slug else request.user.username
            return redirect(reverse('user_profile:view_self_profile', args=[slug]))
        return super(UserProfileView, self).get(request, *args, **kwargs)


class UserSelfProfileView(TemplateView):
    """
    This view for look self profile
    """
    template_name = 'user_profile/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserSelfProfileView, self).get_context_data(**kwargs)
        context['full_name'] = self.request.user.get_full_name()
        return context


class UserRegistrationView(CreateView):
    """
    This view for register user
    """
    template_name = 'user_profile/registration.html'
    model = UserModel
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse('user_profile:login')


class UserAuthorizationView(LoginView):
    """
    This view for login user
    """
    template_name = 'user_profile/login.html'

    def get_success_url(self):
        return reverse('user_profile:view_profile', args=[self.request.user.id])

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super(UserAuthorizationView, self).post(request, *args, **kwargs)
        else:
            return redirect(reverse('main:main_page'))


class UserLogoutView(LogoutView):
    """
    This view for logout user
    """
    next_page = 'main:main_page'
