from django.shortcuts import render
from django.views.generic.base import TemplateView

from rest_framework import viewsets

from .models import SocialUser


class HomePageView(TemplateView):
    template_name = 'home.html'


class UserViewSet(viewsets.ModelViewSet):
    model = SocialUser
