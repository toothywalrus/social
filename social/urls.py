from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from people.views import HomePageView, UserViewSet, HomePageRedirectView,\
    MessageViewSet, UserMessageListView


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'messages', MessageViewSet)

user_urls = patterns('',
                     url(r'^/(?P<user_id>\d+)/messages$',
                         UserMessageListView.as_view(
                         ), name='usermessage-list'),
                     )

urlpatterns = patterns('',
                       url(r'^$', HomePageRedirectView.as_view()),
                       url(r'^api/', include(router.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include(
                           'rest_framework.urls', namespace='rest_framework')),
                       url(r'^home/', HomePageView.as_view(), name='home'),
                       )

urlpatterns += patterns('',
                        url(r'^api/users', include(user_urls)),
                        )
