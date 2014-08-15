from rest_framework import serializers

from .models import SocialUser, Message


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialUser
        fields = ('id', 'username', "skype")


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
