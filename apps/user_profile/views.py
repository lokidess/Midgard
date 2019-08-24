from django.contrib.auth import get_user_model
from django.shortcuts import render

from django.views.generic import TemplateView, CreateView

from apps.user_profile.forms import RegistrationForm
from apps.user_profile.models import UserModel


class UserProfileView(TemplateView):
    template_name = 'user_profile/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['full_name'] = get_user_model().objects.get(id=kwargs['user_id']).get_full_name()
        return context


class UserRegistrationView(CreateView):
    template_name = 'user_profile/registration.html'
    model = UserModel
    form_class = RegistrationForm
