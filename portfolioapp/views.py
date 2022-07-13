from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    success_url = reverse_lazy('portfolioapp:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


