from collections import defaultdict

from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy

from rest_framework import viewsets, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import SocialUser, Message
from .serializers import MessageSerializer


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
        user_id = self.kwargs.get('user_id', self.request.user.id)
        return queryset.filter(Q(sender=user_id) | Q(recipient=user_id))


class OwnerMessageListView(UserMessageListView):
    model = Message
    permission_classes = (permissions.IsAuthenticated,)


class UserConversationList(generics.ListAPIView):
    model = Message

    def get_queryset(self):
        queryset = super(UserConversationList, self).get_queryset()
        user_id = self.kwargs.get('user_id', self.request.user)
        companion_id = self.kwargs['companion_id']
        return queryset.filter(Q(sender=user_id) | Q(recipient=user_id),
                               Q(sender=companion_id) | Q(recipient=companion_id))


class OwnerConversationList(UserConversationList):
    permission_classes = (permissions.IsAuthenticated,)


class OwnerBulkConversationsList(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, format=None):
        return Response(get_user_conversations(request.user))


def get_user_conversations(user):
    messages = Message.objects.filter(Q(sender=user) | Q(recipient=user)).all()

    def partner(two, user_id=user.id):
        return two[0] if two[0] != user_id else two[1]

    conversations = defaultdict(list)
    for message in messages:
        conversations[
            partner((message.sender.id, message.recipient.id))].append(MessageSerializer(message).data)
    return [{'companion': companion, 'messages': messages}
            for companion, messages in conversations.items()]
    # return [message for companion, message in conversations.items()]
    # return conversations.items()
