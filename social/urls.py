from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from people.views import HomePageView, UserViewSet, HomePageRedirectView,\
    MessageViewSet, UserMessageListView, OwnerMessageListView


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
#router.register(r'messages', MessageViewSet)

user_urls = patterns('',
                     url(r'^/(?P<user_id>\d+)/messages$',
                         UserMessageListView.as_view(
                         ), name='usermessage-list'),
                     )

message_urls = patterns('',
                        url(r'^$', OwnerMessageListView.as_view(),
                            name='ownermessages-list'),
                        )

urlpatterns = patterns('',
                       url(r'^$', HomePageRedirectView.as_view()),
                       url(r'^api/', include(router.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include(
                           'rest_framework.urls', namespace='rest_framework')),
                       url(r'^home/$', HomePageView.as_view(), name='home'),
                       )

urlpatterns += patterns('',
                        url(r'^api/users', include(user_urls)),
                        url(r'^api/messages', include(message_urls)),
                        )

urlpatterns += patterns('',
                        url(r'^api/api-token-auth/$',
                            'rest_framework.authtoken.views.obtain_auth_token')
                        )

# urlpatterns = format_suffix_patterns(urlpatterns)
