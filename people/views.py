from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy

from rest_framework import viewsets, generics, permissions

from .models import SocialUser, Message


class HomePageView(TemplateView):
    template_name = 'home.html'


class HomePageRedirectView(RedirectView):
    url = reverse_lazy('home')


class UserViewSet(viewsets.ModelViewSet):
    model = SocialUser


class MessageViewSet(viewsets.ModelViewSet):
    model = Message


class UserMessageListView(generics.ListAPIView):
    model = Message

    def get_queryset(self):
        queryset = super(UserMessageListView, self).get_queryset()
        curr_user = SocialUser.objects.get(pk=1)
        return queryset.filter(Q(sender=curr_user) | Q(recipient=curr_user))
