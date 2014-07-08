from rest_framework import serializers

from .models import SocialUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialUser
        fields = ('id', 'username', "skype")
