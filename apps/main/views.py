from django.shortcuts import render

from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):

        # TODO all remake

        context = super(MainPageView, self).get_context_data(**kwargs)
        context['hello_world'] = 'Hello World!!!'
        return context
