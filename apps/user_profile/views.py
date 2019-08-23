from django.contrib.auth import get_user_model
from django.shortcuts import render

from django.views.generic import TemplateView


class UserProfileView(TemplateView):
    template_name = 'user_profile/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['full_name'] = get_user_model().objects.get(id=kwargs['user_id']).get_full_name()
        return context
