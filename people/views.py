from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy

from rest_framework import viewsets

from .models import SocialUser


class HomePageView(TemplateView):
    template_name = 'home.html'


class HomePageRedirectView(RedirectView):
    url = reverse_lazy('home')


class UserViewSet(viewsets.ModelViewSet):
    model = SocialUser
