from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericRelation,\
    GenericForeignKey

from core.models import TimeStampedModel

user_model = settings.AUTH_USER_MODEL


class SocialUser(AbstractUser):
    # birthday
    # company
    # languages
    # city
    # skype
    skype = models.CharField(max_length=32, null=False, blank=True)
    followers = models.ManyToManyField(
        'self', related_name='followees', symmetrical=False)


class Message(TimeStampedModel):
    sender = models.ForeignKey(user_model, related_name='sent_messages')
    recipient = models.ForeignKey(user_model, related_name='received_messages')
    content = models.TextField()

    def __unicode__(self):
        return "{}".format(self.content[:100])


class Post(TimeStampedModel):
    author = models.ForeignKey(user_model, related_name='posts')
    content = models.TextField()


class Photo(models.Model):
    pass


class Like(models.Model):
    who = models.ForeignKey(user_model, related_name='likes')

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    what = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return "{}'s like for {} with id {}".format(self.who,
                                                    str(self.content_type).capitalize(), self.object_id)


class Activity(models.Model):
    pass
