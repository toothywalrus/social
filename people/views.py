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
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        queryset = super(UserMessageListView, self).get_queryset()
        user_id = self.kwargs['user_id']
        return queryset.filter(Q(sender=user_id) | Q(recipient=user_id))


class OwnerMessageListView(generics.ListAPIView):
    model = Message
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = super(OwnerMessageListView, self).get_queryset()
        return queryset.filter(Q(sender=self.request.user) | Q(recipient=self.request.user))
